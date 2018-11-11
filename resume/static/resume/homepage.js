//onload because otherwise vue will look for el before django renders templates

window.onload = function() {
  var vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
      quote: "An educated man should know everything about something and something about everything. - C.V. Wedgwood"
    },
    methods: {
      get_quote: function (author_name) {
        axios.get('quote/' + author_name)
        .then(function (response) {
          vm.quote = response.data.quotation_text + ' - ' + response.data.author
        })
      }
    }
  });
}
