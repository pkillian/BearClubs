module.exports = function (grunt) {
  
  grunt.loadNpmTasks("grunt-contrib-jshint");
  grunt.loadNpmTasks("grunt-contrib-uglify");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-contrib-cssmin");
  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks("grunt-contrib-copy");
  grunt.loadNpmTasks("grunt-newer");
  grunt.loadNpmTasks('grunt-shell');

  // if you simply run "grunt" these default tasks will execute, IN THE ORDER THEY APPEAR!
  grunt.registerTask('default', ["jshint", "uglify", "less", "cssmin", "copy"]);
  
  // running all the tasks takes more than a couple of seconds, so don't default that
  grunt.registerTask('quick', ["newer:jshint", "newer:uglify", "newer:less", "newer:cssmin", "newer:copy"]);
  
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
        dest: '../bc/static/js/bearclubs.min.js'
      }
    },
    
    less: {
      bearclubs: {
        files: { /* (dest : src) */
          '../src/tmp/main-dark.max.css'  : '../src/less/theme-dark.less',
          '../src/tmp/main-light.max.css' : '../src/less/theme-light.less'
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
          "../bc/static/css/main-dark.min.css": ["../src/tmp/main-dark.max.css"],
          "../bc/static/css/main-light.min.css": ["../src/tmp/main-light.max.css"]
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
              '../src/components/jquery/jquery.min.js'
            ],
            dest: '../bc/static/js/',
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
            dest: '../bc/static/css/',
            filter: 'isFile'
          }
        ]
      },
      img: {
        files: [
          {
            expand: true,
            flatten: true,
            src: [
              '../src/components/jquery.ui/themes/base/images/*'
            ],
            dest: '../bc/static/img/',
            filter: 'isFile'
          }
        ]
      },
      font: {
        files: [
          {
            expand: true,
            flatten: true,
            src: ['../src/components/font-awesome/fonts/*'],
            dest: '../bc/static/font/',
            filter: 'isFile'
          }
        ]
      }
    },
    
    /* watch the development files for saves and do stuff when we observe a save */
    watch: {
      css: {
        files: "<%= '../src/less/**/*' %>",
        tasks: ["less", "cssmin"]
      }
    }
  });
};
