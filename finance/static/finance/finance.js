function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function get_accounts() {
    $.getJSON( "/accounts", function( resp ) {
        var row_div = $('<div>').appendTo('#container');
        row_div.attr('class', 'row');
        var accounts_div = $('<div>').appendTo(row_div);
        accounts_div.attr('class', 'one-half column');
        accounts_div.attr('style', 'margin-top: 5%; margin-left: 5%;');
        var header = $('<h1>').appendTo(accounts_div);
        header.text('Accounts');
        $.each(resp['accounts'], function(key, value) {
            console.log(key + " : " + JSON.stringify(value, null, 2));
            var button = $('<button>').appendTo(accounts_div);
            $('<br>').appendTo(accounts_div);
            button.click(function () {
                $('#container').empty();
                expand_account(value['id']);});
            button.text(value['name']);
        });
    });
}

function expand_account(id) {
    console.log('opening account: ' + id);
    $.getJSON("/accounts/"+id, function(resp) {
      console.log(JSON.stringify(resp));
      var row_div = $('<div>').appendTo('#container');
      row_div.attr('class', 'row');
      var details_div = $('<div>').appendTo(row_div);
      details_div.attr('class', 'one-half column');
      details_div.attr('style', 'margin-top: 5%; margin-left: 5%;');
      var button = $('<button>').appendTo(details_div);
      button.text('back');
      button.click(function() {
            $('#container').empty();
            get_accounts();});
      var header = $('<h1>').appendTo(details_div);
      header.text('Details for '+resp['name']);
      console.log("csrf token: "+getCookie('csrftoken'));
      var upload_button = $('<button>').appendTo(details_div);
      upload_button.text('upload');
      upload_button.click(function() {
        // show upload form
        upload_button.hide();  // only append the form once
        var upload_form = $('<div>').appendTo(details_div);
        $.get("/upload", success=function(data) {
            upload_form.html(data);
        });
      });
    });
}