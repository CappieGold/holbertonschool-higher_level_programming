# JavaScript DOM manipulation

## Learning Objectives
- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

### Sélectionner des éléments HTML en JavaScript
#### Sélectionner des éléments par ID, class et tag name
##### ID:
```bash
const element = document.getElementById('myId');
```

##### Class:
```bash
const elements = document.getElementsByClassName('myClass');
```

##### Tag name:
```bash
const elements = document.getElementsByTagName('div');
```

#### Query Selector (pour des sélections plus flexibles) :
##### Sélectionner un seul élément :
```bash
const element = document.querySelector('#myId');
const element = document.querySelector('.myClass');
const element = document.querySelector('div');
```

##### Sélectionner plusieurs éléments :
```bash
const elements = document.querySelectorAll('.myClass');
```

### Différences entre les sélecteurs ID, class et tag name
- `ID` : Unique dans un document, utilisé pour identifier un seul élément.
- `Class` : Peut être utilisé sur plusieurs éléments, idéal pour appliquer des styles ou des comportements communs.
- `Tag Name` : Sélectionne tous les éléments d'un certain type, utile pour appliquer des actions générales.

### Modifier le style d'un élément HTML
#### Modifier directement le style :
```bash
const element = document.getElementById('myId');
element.style.color = 'red';
element.style.fontSize = '20px';
```

### Obtenir et mettre à jour le contenu d'un élément HTML
#### Obtenir le contenu :
```bash
const element = document.getElementById('myId');
const text = element.textContent; // Pour obtenir le texte
const html = element.innerHTML; // Pour obtenir le HTML
```

#### Mettre à jour le contenu :
```bash
element.textContent = 'Nouveau texte';
element.innerHTML = '<strong>Nouveau contenu</strong>';
```

### Modifier le DOM
#### Ajouter un élément :
```bash
const newElement = document.createElement('div');
newElement.textContent = 'Nouveau div';
document.body.appendChild(newElement);
```

#### Supprimer un élément :
```bash
const element = document.getElementById('myId');
element.remove();
```

### Faire une requête avec XmlHTTPRequest
```bash
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data', true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```

### Faire une requête avec Fetch API
```bash
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### Écouter des événements du DOM
#### Ajouter un écouteur d'événement :
```bash
const button = document.getElementById('myButton');
button.addEventListener('click', function() {
  alert('Button clicked!');
});
```

#### Supprimer un écouteur d'événement :
```bash
function handleClick() {
  alert('Button clicked!');
}
button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick);
```

### Écouter des événements utilisateur
#### Événements courants :
##### Clic:
```bash
button.addEventListener('click', function() {
  alert('Button clicked!');
});
```

##### Survol:
```bash
element.addEventListener('mouseover', function() {
  element.style.backgroundColor = 'yellow';
});
```

##### Saisie clavier:
```bash
const input = document.getElementById('myInput');
input.addEventListener('keydown', function(event) {
  console.log('Key pressed:', event.key);
});
```
