var script = document.createElement('script');

// Set the src attribute to the Bootstrap CDN
script.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js";

// Set the script to load asynchronously
script.async = true;

// Append the script element to the body or head of the document
document.head.appendChild(script);

document.addEventListener('DOMContentLoaded', function () {
    const userIcons = document.querySelectorAll('.user-icon');
    let activeDropdown = null;

    // Function to close all dropdowns
    function closeAllDropdowns() {
        userIcons.forEach(icon => {
            icon.classList.remove('active');
        });
        activeDropdown = null;
    }

    // Handle clicks on user icons
    userIcons.forEach(icon => {
        const toggle = icon.querySelector('.nav-link');
        const dropdown = icon.querySelector('.custom-dropdown');

        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            if (icon.classList.contains('active')) {
                // If clicking active dropdown, close it
                closeAllDropdowns();
            } else {
                // Close other dropdowns and open this one
                closeAllDropdowns();
                icon.classList.add('active');
                activeDropdown = icon;
            }
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.user-icon')) {
            closeAllDropdowns();
        }
    });

    // Handle touch events for mobile
    document.addEventListener('touchstart', (e) => {
        if (!e.target.closest('.user-icon') && !e.target.closest('.custom-dropdown')) {
            closeAllDropdowns();
        }
    });

    // Close dropdown when clicking menu items
    document.querySelectorAll('.dropdown-item').forEach(item => {
        item.addEventListener('click', () => {
            closeAllDropdowns();
        });
    });

    // Close dropdown when clicking close button
    document.querySelectorAll('.downsheet-close').forEach(closeBtn => {
        closeBtn.addEventListener('click', () => {
            closeAllDropdowns();
        });
    });

    // Add smooth scroll for navbar links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Add hover effect for dropdowns
    document.querySelectorAll('.dropdown').forEach(dropdown => {
        dropdown.addEventListener('mouseenter', () => {
            const menu = dropdown.querySelector('.dropdown-menu');
            if (menu) menu.classList.add('show');
        });
        dropdown.addEventListener('mouseleave', () => {
            const menu = dropdown.querySelector('.dropdown-menu');
            if (menu) menu.classList.remove('show');
        });
    });
});
