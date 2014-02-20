var BearClubs = BearClubs || {};

(function(that, $, window, document, undefined) {
    "use strict";

    // false == 60 >= scrollTop > 0
    // true  == scrollTop > 60
    this.scrolled = false;
    this.headerHeight = 60;

    this.bindHeaderScroll = function() {
        // If not scrolled past the header already, and the window scrolls past the header...
        if (!that.scrolled && $(window).scrollTop() > that.headerHeight) {
            
            // Hide the header!
            that.toggleHeader(that.scrolled);
            that.scrolled = true;

        // If scrolled past the header alread, and the window has scrolled above the header...
        } else if (that.scrolled && $(window).scrollTop() <= that.headerHeight) {
            
            // Show the header!
            that.toggleHeader(that.scrolled);
            that.scrolled = false;
        }
    };

    this.toggleHeader = function (toggle) {
        if (toggle) {
            // Show the header
            $('#header').animate({height: that.headerHeight + 'px'}, 'fast', function() {});
        } else {
            // Hide the header
            $('#header').animate({height: '0px'}, 'fast', function() {});
        }
    };

    this.onReady = function() {
        $(window).scroll(that.bindHeaderScroll);
    };

}).call(BearClubs, BearClubs, jQuery, window, document);
