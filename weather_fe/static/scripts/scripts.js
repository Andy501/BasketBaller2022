setInterval(showTime, 1000); 

//for cityh quory try returning array on funciton that changess city ui line 37


// v2 update to local time of form zip
function showTime(){
    let time = new Date();
    let hour = time.getHours();
    let min = time.getMinutes(); 
    let sec = time.getSeconds();
    am_pm = " AM";

    if (hour > 12) {
        hour -= 12;
        am_pm = " PM";
    }
    if (hour == 0) {
        hr = 12;
        am_pm = " AM";
    }

    hour = hour < 10 ? "0" + hour : hour;
    min = min < 10 ? "0" + min : min;
    sec = sec < 10 ? "0" + sec : sec;

    let currentTime = hour + ":"
        + min + ":" + sec + am_pm;

    document.getElementById("Time")
        .innerHTML = currentTime;
}



/*NAvailable cities Miami, New York Los Angeles Miami Chicago */
document.getElementById("city_query0").addEventListener("click", 
function(){
        let city= document.querySelector('#city_query0').value; 
        //ui changes here from async call area?

        //targets city name in ui and writes selected name. 
        let name_ui = document.getElementById("city_name"); 
        name_ui.innerHTML = 'MIAMI';
        return city_choice(city);
         
});

// document.getElementById("city_query1").addEventListener("click", 
// function(){
//         let city= document.querySelector('#city_query1').value; 
//         console.log(city); 


//         let name_ui = document.getElementById("city_name"); 
//         name_ui.innerHTML = 'NEW YORK'; 
//         return city_choice(city);
         
// });


// document.getElementById("city_query2").addEventListener("click", 
// function(){
//         let city= document.querySelector('#city_query2').value; 
//         console.log(city); 

//         let name_ui = document.getElementById("city_name"); 
//         name_ui.innerHTML = 'CHICAGO'; 
//         return city_choice(city);
         
// });

// document.getElementById("city_query3").addEventListener("click", 
// function(){
//         let city= document.querySelector('#city_query3').value; 
//         console.log(city); 

//         let name_ui = document.getElementById("city_name"); 
//         name_ui.innerHTML = 'LOS ANGELES'; 


// 		//set a back tick variable as the returned var and use that in the async call to fetcj
//         return city_choice(city);
         
// });


function city_choice(city){
    let cities = ['miami','newyork', 'chicago','losangeles']; 
    city = cities[city]; 

   
    return city; 

    //need to ask stack how can I call the literal in fetch {city}
}

showTime();

const options = {
	method: 'GET',

};

//js back tick variabl variable. set in city_choice(city) function 
//TODO GRAB City Arg with back ticks returned from celectCity

//todo back tick variable template literal https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
fetch('https://api.openweathermap.org/data/2.5/weather?q=miami&appid=5ad8cdb448dd7bf1414b9ec5cd8c6fc2', options)


.then(response => response.json())

	.then(function(json){
		let farenheit; 
		let attr_;  
		console.log(json)
		farenheit = (json.main.temp - 273.15) * 9/5 + 32
		
		farenheit= Math.floor(farenheit)
		//if rain first condition 
		if (farenheit >= 75){
			attr_ = {"ui":[
				{"temp_desc":"../../hot_af.png"},
				{"temp":"HOT"},
                {"txt_color":"red"}
				]
			}

            document.getElementById("temp_desc").src = attr_['ui'][0].temp_desc
			console.log(attr_['ui'][0].temp_desc)
			console.log(attr_['ui'][1].temp)
		}

		if(farenheit <= 74){
			attr_ = {"ui":[
				{"temp_desc":"../../snow.png"},
				{"temp":"COLD"},
                {"txt_color":"blue"}
				]
			}
            document.getElementById("temp_desc").src = attr_['ui'][0].temp_desc
			console.log(attr_['ui'][0].pic)
			console.log(attr_['ui'][1].temp)
		}
			

		//WORKS	
		
		// }
		document.getElementById("temperature").innerHTML = farenheit + '&#176';
	})
	
	
	.catch(err => console.error(err));


	


// Kelvin to farenheit formula





    


