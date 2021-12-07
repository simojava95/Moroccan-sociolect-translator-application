function darija(let){
  var lettre=let.children[1].innerText;
  document.getElementById("text_in").value=document.getElementById("text_in").value+lettre

}
function bksp(){
 var str = document.getElementById("text_in").value;
  document.getElementById("text_in").value=str.substring(0, str.length-1);
}
function Clear(){
   document.getElementById('text_in').value = "";
   document.getElementById('text_out').value = "";
}
function get_input_text(){
   data=document.getElementById('text_in').value;
   lang=document.getElementById("lang").value;
   eel.start(data,lang);
}


eel.expose(set_output);
function set_output(text){
  document.getElementById('text_out').value=text;
}
