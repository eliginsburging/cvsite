var tablist = ['#home', '#education', '#employment', '#aboutme', '#photography', '#blog']

var vm = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    // QUOTE data
    //===============================
    //===============================
    quote: "An educated man should know everything about something and something about everything.",
    quote_author: "C.V. Wedgwood",
    qauthor_desc: "English historian, author of 'The Thirty Years War,' one of the best-written histories I have ever read",
    sems: [],
    target_sem: '',
    courses: []
  },
  methods: {
    //QUOTE methods
    //================================
    //================================
    get_quote: function (author_name) {
      axios.get('quote/' + author_name)
      .then(function (response) {
        vm.quote = response.data.quotation_text;
        vm.quote_author = response.data.author;
        vm.qauthor_desc = response.data.author_desc;
      })
    },
    show_tab: function (id) {
      $(id).show();
      for (i = 0; i < tablist.length; i++) {
        if (tablist[i] != id) {
          $(tablist[i]).hide();
          $('#tab'+i).removeClass("active");
          $('#tab'+i).addClass("inactive");
        }
        else {
          $('#tab'+i).addClass("active");
          $('#tab'+i).removeClass("inactive");
        }
      }
    },
    get_sems: function () {
      axios.get('semester-list/')
      .then(function (response) {
        vm.sems = response.data;
      });
    },
    get_courses: function (semester_url) {
      vm.courses = []
      vm.target_sem = semester_url
      axios.get(semester_url)
      .then(function (response) {
        for (course_num in response.data.course_set) {
          axios.get(response.data.course_set[course_num])
          .then(function (response) {
            vm.courses.push(response.data)
          })
        }
      })
    }
  }
});
