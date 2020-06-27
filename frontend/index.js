function paramClick(params) {
    // alert("Send params: "+params);
    const xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", 'http://localhost:5000/api/classify');
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    const reqbody = {
        "params": [1, 2, 3, 4]
    }
    xmlhttp.send(JSON.stringify(reqbody));

    console.log("before: " + params);
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4) {
            if (xmlhttp.status === 200) {
                console.log("received answer");
                const text = xmlhttp.responseText;

                showClass(text);
            }
        }
    }
    console.log("after:");
}

function showClass(textAnswer) {
    document.getElementsByClassName("predict")[0].innerText=textAnswer
}