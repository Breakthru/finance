function get_accounts() {
            $.getJSON( "/accounts", function( resp ) {
                var row_div = $('<div>').appendTo('#container');
                row_div.attr('class', 'row');
                var accounts_div = $('<div>').appendTo(row_div);
                accounts_div.attr('class', 'one-half column');
                accounts_div.attr('style', 'margin-top: 25%');
                $.each(resp['accounts'], function(key, value) {
                    console.log(key + " : " + JSON.stringify(value, null, 2));
                    var tmp_span = $('<span>').appendTo(accounts_div);
                    var button = $('<button>').appendTo(tmp_span);
                    button.click(function () {expand_account(value['id']);});
                    button.text(value['name']);
                });
            });
        }

        function expand_account(id) {
            console.log('opening account: ' + id);
            $.getJSON("/accounts/"+id, function(resp) {
              console.log(JSON.stringify(resp));
            });
        }