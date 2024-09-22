document.addEventListener('DOMContentLoaded',
    /**
     * This function initializes the responsive behavior of the navigation bar.
     * It adds a click event listener to the navbar toggler element, which toggles the collapse class on the navbar collapse element.
     *
     * @function
     * @returns {void}
     */
    function() {
        /**
         * The navbar toggler element.
         * @type {HTMLElement}
         */
        const toggler = document.querySelector('.navbar-toggler');

        /**
         * The navbar collapse element.
         * @type {HTMLElement}
         */
        const navbarCollapse = [document.querySelector('#navbarNavLeft'), document.querySelector('#navbarNavRight')];

        toggler.addEventListener('click', function() {
            /**
             * Toggles the 'collapse' class on the navbar collapse element.
             */
            for (item in navbarCollapse) {
                navbarCollapse[item].classList.toggle('collapse');
            }

        });
    });