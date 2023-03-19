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



$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'{{forum.id}}/send',
      data:{
        message:$('#message').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
         //alert(data)
      }
    });
    document.getElementById('message').value = ''
  });


  
