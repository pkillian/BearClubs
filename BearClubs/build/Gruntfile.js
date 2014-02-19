module.exports = function (grunt) {
  
  grunt.loadNpmTasks("grunt-contrib-jshint");
  grunt.loadNpmTasks("grunt-contrib-uglify");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-contrib-cssmin");
  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks("grunt-contrib-copy");

  // if you simply run "grunt" these default tasks will execute, IN THE ORDER THEY APPEAR!
  grunt.registerTask('default', ["jshint", "uglify", "less", "cssmin", "copy"]);
  
  // running all the tasks takes more than a couple of seconds, so don't default that
  grunt.registerTask('quick', ["jshint", "uglify:bearclubs", "copy:templates", "copy:js"]);
  
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    
    // ##################### JAVASCRIPT ############################ //
    
    /* http://www.jshint.com/options/ */
    jshint: {
      files: ['../src/js/**/*.js'],
      options: {
        jshintrc: '.jshintrc'
      }
    },

    uglify: { // only uglify what needs to be uglified
      options: {
        banner: '/* generated: <%= grunt.template.today("yyyy-mm-dd @ HH:MM:ss") %> */\n'
      },
      bearclubs: {
        src: ['../src/js/bearclubs.js', '../src/js/**/*.js'],
        dest: '../BearClubs/static/js/bearclubs.min.js'
      }
    },
    
    less: {
      bearclubs: {
        files: { /* (dest : src) */
          '../src/tmp/main.max.css' : '../src/less/main.less'
        },
        options: {
          paths: ['../src/less']
        }
      }
    },
    
    /* (dest : [src, src]) */
    cssmin: {
      compress: {
        files: {
          "../BearClubs/static/css/main.min.css": ["../src/tmp/main.max.css"]
        }
      }
    },
    
    copy: {
      js: { // any files that were minified by the authors should be in here
        files: [
          {
            expand: true,
            flatten: true,
            src: [
              // '../src/components/jquery.ui/jquery-ui.min.js',
              '../src/components/jquery/jquery.min.js'
            ],
            dest: '../BearClubs/static/js/',
            filter: 'isFile'
          }
        ]
      },
      css: {
        files: [
          {
            expand: true,
            flatten: true,
            src: [
              '../src/components/font-awesome/css/font-awesome.min.css',
            ],
            dest: '../BearClubs/static/css/',
            filter: 'isFile'
          }
        ]
      },
      // img: {
      //   files: [
      //     {
      //       expand: true,
      //       flatten: true,
      //       src: [
      //         '../src/components/jquery.ui/themes/base/images/*'
      //       ],
      //       dest: '../BearClubs/static/images/',
      //       filter: 'isFile'
      //     }
      //   ]
      // },
      font: {
        files: [
          {
            expand: true,
            flatten: true,
            src: ['../src/components/font-awesome/fonts/*'],
            dest: '../BearClubs/static/font/',
            filter: 'isFile'
          }
        ]
      }
    },
    
    /* watch the development files for saves and do stuff when we observe a save */
    watch: {
      css: {
        files: "<%= '../src/less/**/*' %>",
        tasks: ["reload"]
      }
    }
  });
};
