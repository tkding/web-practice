if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}


function count(){
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        // in python it's f"Counter is now {counter}"
        alert(`Counter is now ${counter}`);
    }
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    //setInterval(count, 1000);
});
