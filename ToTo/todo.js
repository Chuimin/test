function add(){
    var text = document.getElementById("put").value;
    console.log(text)
}
var todo = new Vue({
    el : '#bd',
    data:{
        'id' : 0,
        'text' : '',
        'status' : false
    } 
})
var todolist = [];