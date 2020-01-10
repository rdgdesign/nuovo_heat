
function controllaT(t) {
	$("#contactForm").submit(function(e, num){
		e.preventDefault();
		})
	var box = document.querySelector("#rischio")
        
        if(box) {
            box.classList.remove("d-block")
            box.classList.add("d-none")
        }

        var temperatura = t
        // alert(temperatura)
        // var umidita = u
        
		var err_temp = document.getElementById("error_temp")
		var err_max_temp = document.getElementById("error_max_temp")
        var err_umid = document.getElementById("error_umid")
        var minimo_temp = 26.6 
		var minmo_umidita = 39
		var max_temp = 43.4
		var max_umid = 110

       if( temperatura < minimo_temp ) {
		   
            err_temp.classList.remove("d-none")
			err_temp.classList.add("d-block")
			verotemp = false
		} 
			 else if (temperatura > max_temp) 
			{
				
				err_temp.classList.remove('d-block')
				err_temp.classList.add('d-none')

				err_max_temp.classList.remove("d-none")
				err_max_temp.classList.add("d-block")
				verotemp = false
			}
				else 
				{
					err_max_temp.classList.remove("d-block")
					err_max_temp.classList.add("d-none")
				
					err_temp.classList.remove('d-block')
					err_temp.classList.add('d-none')

					err_umid.classList.remove('d-block')
					err_umid.classList.add('d-none')
					verotemp = true
				}
}

function controllaU(u) {
	
	var box = document.querySelector("#rischio")
        
        if(box) {
            box.classList.remove("d-block")
            box.classList.add("d-none")
        }

        var umidita = u
        // var umidita = u
        
        var err_temp = document.getElementById("error_temp")
		var err_umid = document.getElementById("error_umid")
		var err_max_umid = document.getElementById("error_max_umid")
        var minimo_temp = 27.6 
		var minimo_umidita = 40
		var max_temp = 43.3
		var max_umid = 110

       if( umidita < minimo_umidita ) {
		$("#contactForm").submit(function(e, num){
		e.preventDefault();
		})
		   
            err_umid.classList.remove("d-none")
			err_umid.classList.add("d-block")
			veroumid = false
		} 
		else if (umidita > max_umid) 
			{
				
				err_umid.classList.remove("d-block")
				err_umid.classList.add("d-none")
				
				err_max_umid.classList.remove("d-none")
				err_max_umid.classList.add("d-block")
				veroumid = false
			}

		else {
			err_max_umid.classList.remove("d-block")
			err_max_umid.classList.add("d-none")

			err_umid.classList.remove('d-block')
            err_umid.classList.add('d-none')
			veroumid = true
		}
}
