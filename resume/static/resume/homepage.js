var tablist = ['#home', '#education', '#employment', '#volunteer', '#projects', '#aboutme', '#photography', '#blog']

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
    show_transcript: false,
    target_sem: '',
    courses: [],
    awards: [],
    apcourses: [],
    current_lang: [],
    past_lang: [],
    lang_details: [],
    target_lang: '',
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
      console.log(id)
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
      if (id == "#education" && this.awards.length == 0) {
        this.get_awards();
        this.get_apcourses();
        this.get_currentlang();
        this.get_pastlang();
      }
    },
    get_sems: function () {
      vm.show_transcript = true;
      axios.get('semester-list/')
      .then(function (response) {
        vm.sems = response.data;
      });
    },
    hide_transcript: function () {
      vm.show_transcript = false;
    },
    toggle_course: function (course_name) {
      $(course_name).toggle()
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
    },
    get_awards: function () {
      vm.awards = []
      axios.get('award-list')
      .then(function (response) {
        for (award_num in response.data) {
          vm.awards.push(response.data[award_num])
        }
      })
    },
    get_apcourses: function () {
      vm.apcourses = []
      axios.get('apcourse-list')
      .then(function (response) {
        for (apcourse_num in response.data) {
          vm.apcourses.push(response.data[apcourse_num])
        }
      })
    },
    get_currentlang: function () {
      vm.current_lang = []
      axios.get('language-list/current')
      .then(function (response) {
        for (num in response.data) {
          vm.current_lang.push(response.data[num])
        }
      })
    },
    get_pastlang: function () {
      vm.past_lang = []
      axios.get('language-list/past')
      .then(function (response) {
        for (num in response.data) {
          vm.past_lang.push(response.data[num])
        }
      })
    },
    get_langdetails: function (target_lang, lang_id) {
      vm.target_lang = target_lang
      vm.lang_details = []
      axios.get('language/'+lang_id)
      .then(function (response) {
        for (det in response.data.languagedetail_set) {
          axios.get(response.data.languagedetail_set[det])
          .then(function (response) {
            vm.lang_details.push(response.data.detail)
          })
        }
        $(target_lang).toggle()

      })
    }
  }
});
