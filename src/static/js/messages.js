$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type: 'GET',
          url : "{{forum.id}}/getMessages",
            success: function(response){
                console.log(response);
                $("#display").empty();
                for (var key in response.messages)
                {
                    var temp="<div class='container darker'><b>"+
                            response.messages[key].commenter__username+"</b><p>"+
                            response.messages[key].message+"</p><span class='time-left'>"+
                            response.messages[key].timestamp+"</span></div>";
                    $("#display").append(temp);
                }
            },
            error: function(response,){
              alert('An error occured')
            }
        });
  },1000);
})
