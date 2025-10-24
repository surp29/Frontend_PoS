from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import Config
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)

# Tắt auto-load .env file
app.config['LOAD_DOTENV'] = False

# Inject BACKEND_URL to all templates
@app.context_processor
def inject_backend_url():
    return { 'BACKEND_URL': Config.BACKEND_URL }

# Decorator để kiểm tra user đã đăng nhập
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vui lòng đăng nhập để tiếp tục', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes - chỉ render templates, không có logic API

@app.route('/')
@login_required
def index():
    """Trang chủ - chuyển hướng đến nhật ký chung"""
    return redirect(url_for('general_diary'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Trang đăng nhập"""
    if request.method == 'POST':
        # Logic đăng nhập sẽ được xử lý bởi JavaScript
        pass
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Đăng xuất"""
    session.clear()
    flash('Bạn đã đăng xuất thành công', 'success')
    return redirect(url_for('login'))

@app.route('/products')
@login_required
def products():
    """Trang quản lý sản phẩm"""
    return render_template('products.html')

@app.route('/orders')
@login_required
def orders():
    """Trang quản lý đơn hàng"""
    return render_template('orders.html')

@app.route('/invoices')
@login_required
def invoices():
    """Trang quản lý hóa đơn"""
    return render_template('invoices.html')

@app.route('/warehouse')
@login_required
def warehouse():
    """Trang quản lý kho hàng"""
    return render_template('warehouse.html')

@app.route('/prices')
@login_required
def prices():
    """Trang quản lý bảng giá"""
    return render_template('prices.html')

@app.route('/product-groups')
@login_required
def product_groups():
    """Trang quản lý nhóm sản phẩm"""
    return render_template('product_groups.html')

@app.route('/general-diary')
@login_required
def general_diary():
    """Trang nhật ký chung"""
    return render_template('general_diary.html')

@app.route('/reports')
@login_required
def reports():
    """Trang báo cáo"""
    return render_template('reports.html')

@app.route('/areas-management')
@login_required
def areas_management():
    """Trang tạo và quản lý khu vực"""
    return render_template('areas_management.html')

@app.route('/shops-management')
@login_required
def shops_management():
    """Trang tạo và quản lý shop"""
    return render_template('shops_management.html')

@app.route('/account-management')
@login_required
def account_management():
    """Trang quản lý tài khoản"""
    return render_template('account_management.html')

if __name__ == '__main__':
    print("🚀 Starting PhanMemKeToan Frontend on port", Config.FRONTEND_PORT)
    print("🌐 Frontend will be available at: http://localhost:" + str(Config.FRONTEND_PORT))
    print("🔗 Backend API: " + Config.BACKEND_URL)
    print("💡 Use Ctrl+C to stop the server")
    print()
    
    app.run(
        host=Config.HOST,
        port=Config.FRONTEND_PORT,
        debug=Config.DEBUG
    )