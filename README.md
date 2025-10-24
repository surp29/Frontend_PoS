# PhanMemKeToan Frontend

## 🎨 Flask Frontend Application

Frontend application được xây dựng với Flask, cung cấp giao diện người dùng cho hệ thống quản lý bán hàng PhanMemKeToan.

## 📋 Tính năng

### 🎯 User Interface
- **Responsive Design**: Tương thích mọi thiết bị
- **Modern UI**: Giao diện hiện đại, thân thiện
- **Interactive Elements**: Tương tác mượt mà
- **Real-time Updates**: Cập nhật real-time

### 📊 Management Pages
- **Products Management**: Quản lý sản phẩm
- **Orders Management**: Quản lý đơn hàng
- **Invoices Management**: Quản lý hóa đơn
- **Prices Management**: Quản lý giá cả
- **Warehouse Management**: Quản lý kho hàng
- **General Diary**: Nhật ký chung
- **Reports**: Báo cáo thống kê
- **Areas Management**: Quản lý khu vực
- **Shops Management**: Quản lý shop
- **Account Management**: Quản lý tài khoản

## 🛠️ Cài đặt

### Yêu cầu
- Python 3.8+
- pip
- Modern web browser

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Chạy application
```bash
python app.py
```

## 🌐 Truy cập

- **Application**: http://localhost:5000
- **Login Page**: http://localhost:5000/login

## 📁 Cấu trúc thư mục

```
Frontend/
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── login.html         # Login page
│   ├── products.html      # Products management
│   ├── orders.html        # Orders management
│   ├── invoices.html      # Invoices management
│   ├── prices.html        # Prices management
│   ├── warehouse.html     # Warehouse management
│   ├── general_diary.html # General diary
│   ├── reports.html       # Reports
│   ├── areas_management.html # Areas management
│   ├── shops_management.html # Shops management
│   └── account_management.html # Account management
├── static/                 # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/                # JavaScript files
│   └── images/            # Images
│       ├── logo.png       # Main logo
│       └── LogoPoS.png    # POS logo
├── app.py                 # Flask application
├── config.py              # Configuration
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## 🎨 UI Components

### Layout Components
- **Header**: Navigation bar với logo và menu
- **Sidebar**: Menu điều hướng chính
- **Content**: Nội dung chính của trang
- **Footer**: Thông tin footer

### Form Components
- **Input Fields**: Text, number, date, email
- **Select Dropdowns**: Dropdown menus
- **Textareas**: Multi-line text input
- **Buttons**: Action buttons với icons
- **Modals**: Popup dialogs

### Data Components
- **Tables**: Data tables với pagination
- **Cards**: Information cards
- **Statistics**: Dashboard statistics
- **Charts**: Data visualization

## 🔧 Cấu hình

### Environment Variables
Tạo file `.env`:
```env
BACKEND_URL=http://localhost:5001
SECRET_KEY=your-secret-key-here
DEBUG=True
HOST=0.0.0.0
PORT=5000
```

### Configuration
```python
# config.py
BACKEND_URL = "http://localhost:5001"
SECRET_KEY = "your-secret-key"
DEBUG = True
```

## 🎯 Pages Overview

### Login Page (`/login`)
- **Purpose**: User authentication
- **Features**: Username/password login, error handling
- **Redirect**: After login → General Diary page

### Products Management (`/products`)
- **Purpose**: Manage products and product groups
- **Features**: CRUD operations, search, filter, pagination
- **Components**: Product table, add/edit modals

### Orders Management (`/orders`)
- **Purpose**: Manage customer orders
- **Features**: Order creation, status tracking, customer info
- **Components**: Order table, order form, status updates

### Invoices Management (`/invoices`)
- **Purpose**: Manage invoices and billing
- **Features**: Invoice generation, payment tracking
- **Components**: Invoice table, invoice form, payment status

### Prices Management (`/prices`)
- **Purpose**: Manage product pricing
- **Features**: Price setting, price history, bulk updates
- **Components**: Price table, price form, price calculator

### Warehouse Management (`/warehouse`)
- **Purpose**: Manage inventory and stock
- **Features**: Stock tracking, inventory reports, alerts
- **Components**: Inventory table, stock form, alerts

### General Diary (`/general-diary`)
- **Purpose**: Financial transaction logging
- **Features**: Transaction recording, account management
- **Components**: Transaction form, account table, reports

### Reports (`/reports`)
- **Purpose**: Generate business reports
- **Features**: Sales reports, inventory reports, financial reports
- **Components**: Report filters, charts, export options

### Areas Management (`/areas-management`)
- **Purpose**: Manage geographical areas
- **Features**: Area creation, management, shop assignment
- **Components**: Area table, area form, shop assignment

### Shops Management (`/shops-management`)
- **Purpose**: Manage shop locations
- **Features**: Shop creation, management, area assignment
- **Components**: Shop table, shop form, area selection

### Account Management (`/account-management`)
- **Purpose**: Manage user accounts
- **Features**: User creation, role management, permissions
- **Components**: User table, user form, role assignment

## 🎨 Styling

### CSS Framework
- **Custom CSS**: Tailored for PhanMemKeToan
- **Responsive Design**: Mobile-first approach
- **Modern UI**: Clean, professional design
- **Color Scheme**: Consistent color palette

### Key Styles
```css
/* Color Variables */
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --success-color: #27ae60;
    --warning-color: #f39c12;
    --danger-color: #e74c3c;
    --light-color: #ecf0f1;
    --dark-color: #2c3e50;
}

/* Component Styles */
.card { /* Card components */ }
.modal { /* Modal dialogs */ }
.table { /* Data tables */ }
.form { /* Form elements */ }
.btn { /* Buttons */ }
```

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Mobile Features
- **Touch-friendly**: Large touch targets
- **Swipe gestures**: Navigation gestures
- **Mobile menu**: Collapsible sidebar
- **Optimized forms**: Mobile-optimized inputs

## 🔌 API Integration

### Backend Communication
- **RESTful API**: Communication với FastAPI backend
- **Authentication**: JWT token management
- **Error Handling**: Comprehensive error handling
- **Loading States**: User feedback during API calls

### API Calls
```javascript
// Example API call
async function fetchProducts() {
    try {
        const response = await fetch(`${BACKEND_URL}/api/products/`, {
            headers: {
                'Authorization': `Bearer ${sessionStorage.getItem('access_token')}`
            }
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching products:', error);
        throw error;
    }
}
```

## 🎯 JavaScript Features

### Core Functions
- **API Communication**: Fetch API với error handling
- **Form Validation**: Client-side validation
- **Modal Management**: Modal open/close logic
- **Data Filtering**: Search và filter functionality
- **Pagination**: Table pagination
- **Real-time Updates**: Live data updates

### Utility Functions
```javascript
// Form validation
function validateForm(form) { /* Validation logic */ }

// Modal management
function openModal(modalId) { /* Modal open */ }
function closeModal(modalId) { /* Modal close */ }

// Data formatting
function formatMoney(amount) { /* Money formatting */ }
function formatDate(date) { /* Date formatting */ }
```

## 🧪 Testing

### Frontend Testing
```bash
python -m pytest tests/
```

### Browser Testing
- **Chrome**: Latest version
- **Firefox**: Latest version
- **Safari**: Latest version
- **Edge**: Latest version

### Mobile Testing
- **iOS Safari**: Mobile testing
- **Android Chrome**: Mobile testing
- **Responsive Design**: Cross-device testing

## 🚀 Performance

### Optimization
- **Minified CSS**: Compressed stylesheets
- **Optimized Images**: Compressed images
- **Lazy Loading**: Deferred loading
- **Caching**: Browser caching

### Performance Metrics
- **Load Time**: < 2 seconds
- **First Paint**: < 1 second
- **Interactive**: < 3 seconds
- **Lighthouse Score**: 90+

## 🔒 Security

### Frontend Security
- **Input Validation**: Client-side validation
- **XSS Prevention**: Output escaping
- **CSRF Protection**: Token validation
- **Secure Headers**: Security headers

### Authentication
- **JWT Tokens**: Secure token management
- **Session Storage**: Secure storage
- **Auto Logout**: Session timeout
- **Role-based Access**: Permission-based UI

## 📚 Documentation

### Code Documentation
- **Inline Comments**: Detailed code comments
- **Function Documentation**: JSDoc-style comments
- **API Documentation**: API usage examples
- **Component Documentation**: Component usage

### User Documentation
- **User Manual**: Step-by-step guides
- **Video Tutorials**: Video demonstrations
- **FAQ**: Frequently asked questions
- **Support**: Contact information

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker
```bash
docker build -t phanmemketoan-frontend .
docker run -p 5000:5000 phanmemketoan-frontend
```

## 🔧 Troubleshooting

### Common Issues
1. **Backend Connection Error**
   - Check backend URL configuration
   - Verify backend server is running
   - Check network connectivity

2. **Authentication Error**
   - Check JWT token validity
   - Verify user credentials
   - Check session storage

3. **UI Rendering Issues**
   - Check CSS file loading
   - Verify JavaScript errors
   - Check browser compatibility

## 📞 Support

- **Documentation**: [Frontend Docs](http://localhost:5000/docs)
- **Issues**: [GitHub Issues](https://github.com/phanmemketoan/issues)
- **Email**: support@phanmemketoan.com

---

**PhanMemKeToan Frontend** - Professional Flask Application