// $("#contactForm").submit(function(e, num){
//     e.preventDefault();


//     var temperatura = $("#id_temperatura").val();
//     var umidita = $("#id_umidita").val();
//     var text = document.querySelector("#contactForm > p:nth-child(3) > label").innerText
//     var unita = text.search(" °C")
    
//     if(unita > 0) {
//         temperatura = (temperatura * 9/5) + 32 
//         $("#contactForm > p:nth-child(3) > label").append(temperatura)
//     } else {
//         temperatura = temperatura
//     }
    
//     // var temperatura = $("#id_temperatura").val();
//     // temperatura = temperatura * 2
    
    
    
    
    
//     // alert(temperatura)
//     var serializedData = $(this).serialize();
//     // alert(serializedData)
//     $.ajax({
//         type : 'POST',
//         url :  "{% url 'contact_submit' %}",
//         // data : serializedData,
//         data : {"csrfmiddlewaretoken" : "{{csrf_token}}", temperatura : temperatura, umidita : umidita},
//         // dataType : 'json',
//         // data : { "temperatura" : $("#id_temperatura").val()}
//         success : function(data){
//             $("#contactForm")[0].reset();
//             document.querySelector("#contactForm > p:nth-child(3) > label").innerText = "Temperatura"
            

//             $('#response').html(data);
//             var ris = $("#response").text()
//             ris = parseFloat(ris)
//             rischio(ris)
//             // console.log(response);
//             // alert(response);
//             // var text = response.innerHTML
//             // document.getElementById("response").innerHTML = text
            
        
//         },
//         error : function(response){
//             console.log(response)
//         }
//     })
// })


