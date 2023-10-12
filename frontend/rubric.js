// const domain = 'http://localhost:8000/';
const domain = 'http://127.0.0.1:8000/';

// let list = document.getElementById('list');
let list = document.querySelector('#list');
let listLoader = new XMLHttpRequest();

let id = document.querySelector('#id');
let name = document.querySelector('#name');
let rubricLoader = new XMLHttpRequest();

let rubricUpdater = new XMLHttpRequest();
let rubricDeleter = new XMLHttpRequest();

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>';
            for (let i = 0; i < data.length; i++) {
                d = data[i];
                s += '<li>' + d.name + ' <a href="' + domain +
                     'api/rubrics/' + d.id +
                     '/" class="detail">Вывести</a> <a href="' + domain +
                     'api/rubrics/' + d.id +
                     '/" class="delete">Удалить</a></li>';
            }
            s += '</ul>';
            list.innerHTML = s;

            let links = list.querySelectorAll('ul li a.detail');
            links.forEach((link) => {
                link.addEventListener('click', rubricLoad);
            });

            links = list.querySelectorAll('ul li a.delete');
            links.forEach((link) => {
                link.addEventListener('click', rubricDelete);
            });

        } else
            console.log(listLoader.status, listLoader.statusText);
    }
});

rubricLoader.addEventListener('readystatechange', () => {
    if (rubricLoader.readyState == 4) {
        if (rubricLoader.status == 200) {
            let data = JSON.parse(rubricLoader.responseText);
            id.value = data.id;
            name.value = data.name;
        } else
            console.log(rubricLoader.status, rubricLoader.statusText);
    }
});

rubricUpdater.addEventListener('readystatechange', () => {
    if (rubricUpdater.readyState == 4) {
        if ((rubricUpdater.status == 200) || (rubricUpdater.status == 201)) {
            listLoad();
            name.form.reset();
            id.value = '';
        } else
            console.log(rubricLoader.status, rubricLoader.statusText);
    }
});

name.form.addEventListener('submit', (evt) => {
    evt.preventDefault();
    let vid = id.value, url, method;
    if (vid) {
        url = 'api/rubrics/' + vid + '/';
        method = 'PUT';
    } else {
        url = 'api/rubrics/';
        method = 'POST';
    }

    let data = JSON.stringify({id: vid, name: name.value});
    rubricUpdater.open(method, domain + url, true);
    rubricUpdater.setRequestHeader('Content-Type', 'application/json');

    // data = 'id=' + encodeURIComponent(vid);
    // data += '&name=' + encodeURIComponent(name.value);
    // rubricUpdater.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    rubricUpdater.send(data);
});

rubricDeleter.addEventListener('readystatechange', () => {
    if (rubricDeleter.readyState == 4) {
        if (rubricDeleter.status == 204) {
            listLoad();
        } else {
            console.log(rubricDeleter.status, rubricDeleter.statusText);
        }
    }
});

function listLoad() {
    listLoader.open('GET', domain + 'api/rubrics/', true);
    listLoader.send();
}

function rubricLoad(evt) {
    evt.preventDefault();
    rubricLoader.open('GET', evt.target.href, true);
    rubricLoader.send();
}

function rubricDelete(evt) {
    evt.preventDefault();
    rubricDeleter.open('DELETE', evt.target.href, true);
    rubricDeleter.send();
}

listLoad();