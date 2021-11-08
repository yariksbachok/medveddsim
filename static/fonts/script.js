


function filter_chagne(event){
	const items = document.querySelector('.update_num_container').children
	if(event.value === '01'){
		for( item of items){
			item.classList.remove("no_show")
			item.classList.add("show")
		}
		return
	}

	id = event.value;



	for( item of items){

		console.log(item)
		if(item.getAttribute('item_id') != id){
			item.classList.add("no_show")
			item.classList.remove("show")
		}else if(item.getAttribute('item_id') === id){
			item.classList.remove("no_show")
			item.classList.add("show")
		}
	}

}

function myFunction(){
    var element = document.querySelector(".just_ul");
    element.classList.toggle("activeete");
}
function myuser(){
    var element = document.querySelector(".user_ul");
    element.classList.toggle("active");
}
