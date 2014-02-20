var BearClubs = BearClubs || {};

(function(that, $, window, document, undefined) {
    "use strict";

    // false == 60 >= scrollTop > 0
    // true  == scrollTop > 60
    this.scrolled = false;
    this.headerShown = true;
    this.headerHeight = 60;

    this.bindHeaderMouseOver = function(ev) {
        // If the page is scrolled, the header isn't shown, and the mouse is between 0-80...
        if (that.scrolled && !that.headerShown && ev.clientY <= that.headerHeight + 20) {

            // Show the header!
            that.toggleHeader(true);

        // If the page is scrolled, the header is shown, and the mouse is between 81-inf...
        } else if (that.scrolled && that.headerShown && ev.clientY > that.headerHeight + 20) {
            
            // Hide the header
            that.toggleHeader(false);
        }
    };

    this.bindHeaderScroll = function() {
        // If not scrolled past the header already, and the window scrolls past the header...
        if (!that.scrolled && $(window).scrollTop() > that.headerHeight) {
            
            // Hide the header!
            that.toggleHeader(false);
            that.scrolled = true;

        // If scrolled past the header alread, and the window has scrolled above the header...
        } else if (that.scrolled && $(window).scrollTop() <= that.headerHeight) {
            
            // Show the header!
            that.toggleHeader(true);
            that.scrolled = false;
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
