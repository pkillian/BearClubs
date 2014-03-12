var BearClubs = BearClubs || {};

(function(that, $, window, document, undefined) {
    "use strict";

    // false == 60 >= scrollTop > 0
    // true  == scrollTop > 60
    this.scrolled = false;
    this.mousedOver = false;
    this.headerShown = true;
    this.headerHeight = 60;
    this.photoScrollers = {};

    this.bindHeaderMouseOver = function(ev) {
        that.mousedOver = (ev.clientY <= that.headerHeight + 20);

        // If the page is scrolled, the header isn't shown, and the mouse is between 0-80...
        if (that.scrolled && !that.headerShown && that.mousedOver) {

            // Show the header!
            that.toggleHeader(true);

        // If the page is scrolled, the header is shown, and the mouse is between 81-inf...
        } else if (that.scrolled && that.headerShown && !that.mousedOver) {

            // Hide the header
            that.toggleHeader(false);
        }
    };

    this.bindHeaderScroll = function(ev) {
        that.scrolled = ($(window).scrollTop() > that.headerHeight);

        if (that.mousedOver) {
            return false;
        }

        // If not scrolled past the header already, and the window scrolls past the header...
        if (that.headerShown && that.scrolled) {

            // Hide the header!
            that.toggleHeader(false);

        // If scrolled past the header already, and the window has scrolled above the header...
        } else if (!that.headerShown && !that.scrolled) {

            // Show the header!
            that.toggleHeader(true);

        }
    };

    this.toggleHeader = function (toggle) {
        if (toggle) {
            // Show the header
            $('#header').animate({height: that.headerHeight + 'px'}, 'fast', function() {
                $('#header').css('border-bottom-style', 'solid');
            });
        } else {
            // Hide the header
            $('#header').animate({height: '0px'}, 'fast', function() {
                $('#header').css('border-bottom-style', 'none');
            });
        }

        that.headerShown = toggle;
    };

    this.onReady = function() {
        $(window).scroll(that.bindHeaderScroll);
        $(window).mousemove(that.bindHeaderMouseOver);
    };

}).call(BearClubs, BearClubs, jQuery, window, document);
