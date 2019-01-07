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
    skills: [],
    positions: [],
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
      if (id == "#education" && this.awards.length == 0) {
        this.get_awards();
        this.get_apcourses();
        this.get_currentlang();
        this.get_pastlang();
        this.get_skills();
      }
    },
    get_skills: async function () {
      // build a list of nested JSON objects
      // the "skill_obj" key of each json object will be associated with the
      // JSON for a single skill (as retrieved from the api).
      // the "skill_list" key of each json object will be associated with a list
      // of details crresponding to that skill

      const skill_list = await axios.get('skill-list/')
      skill_list.data.forEach(function(skillObj){
        var temp_dict = {}
        var temp_sublist = []
        temp_dict.skill_obj = skillObj // push whole json response as first item in list
        skillObj.skilldetail_set.forEach(async function(detURL) {
          const detail = await axios.get(detURL)
          temp_sublist.push(detail.data.skill_detail)
        })
        temp_dict.skill_list = temp_sublist // second item in temp_list is a list with eacg skill detail
        vm.skills.push(temp_dict)
      })
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
    },
    get_positions: async function() {
      // build a list of json objects
      // each json object will have the following key value pairs:
      // 'position_obj' --> full json response for an api call on a position
      // 'prior_titles' --> list of prior title json objects associated with the positions
      // 'duties' --> a list of json objects, each as follows:
      //     'duty' --> text of a single duty
      //     'tags' --> list of tags associated with the duty
      // 'projects' --> a list of json objects, each as follows:
      //     'project_name' --> name of a single project
      //     'project_desc' --> text of a single project
      //     'tags' --> a list of tags associated with the project
      var master_list = []
      const pos_list = await axios.get('position-list')
      //first, loop through each json object in our position list
      pos_list.data.forEach(function(posObj){
        var projlist_jsonObj = {}
        // this is the larger json object described above,
        // which will eventually be pushed into the master list
        projlist_jsonObj['position_obj'] = posObj
        var title_list = []
        // build a list of prior title objects
        // (rather than the urls returned in our first axios call above)
        posObj.priortitle_set.forEach(async function(pturl){
          const titleObj = await axios.get(pturl)
          title_list.push(titleObj.data)
        })
        projlist_jsonObj['prior_titles'] = title_list
        // build a list of duty objects (rather than the
        // urls returned by our initial axios call above)
        var duties_list = []
        posObj.duty_set.forEach(async function(dutyurl){
          var duty_dict = {}
          const dutyObj = await axios.get(dutyurl)
          duty_dict['duty'] = dutyObj.data.job_duty
          // text of a single duty
          var dutytag_list = []
          // create a list of tags associated with that text
          dutyObj.data.dutytag_set.forEach(async function(dtagurl){
            const dutytagObj = await axios.get(dtagurl)
            console.log(dutytagObj.data.duty_tag)
            dutytag_list.push(dutytagObj.data.duty_tag)
            console.log(dutytag_list)
          })
          console.log(dutytag_list)
          duty_dict['tags'] = dutytag_list
          duties_list.push(duty_dict)
        })
        projlist_jsonObj['duties'] = duties_list
        // build a list of projects (rather than the urls returned by
        // the initial axios call)
        var projects_list = []
        posObj.project_set.forEach(async function(projurl){
          var proj_dict = {}
          const projObj = await axios.get(projurl)
          proj_dict['project_name'] = projObj.data.project_name
          proj_dict['project_desc'] = projObj.data.project_description
          var projtag_list = []
          projObj.data.projecttag_set.forEach(async function(ptagurl){
            const ptagObj = await axios.get(ptagurl)
            projtag_list.push(ptagObj.data.project_tag)
          })
          proj_dict['tags'] = projtag_list
          projects_list.push(proj_dict)
        })
        projlist_jsonObj['projects'] = projects_list
        master_list.push(projlist_jsonObj)
      })
      vm.positions = master_list
    }
  }
});
