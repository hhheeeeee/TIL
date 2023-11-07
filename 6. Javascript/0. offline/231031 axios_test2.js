const makeListItem = function(article) {
  const ulElement = document.querySelector('#article-list')
  // craete 하기 전에 있는 거라면 pass, 없는 거라면 생성
  if (!document.querySelector(`#article-${article.id}`)){
    const liElement = document.createElement('li')
    liElement.textContent = `${article.id} - ${article.content}`
    // liElement 하나하나에 id 지정
    liElement.id = `article-${article.id}`

    ulElement.appendChild(liElement)

    const deleteBtn = document.createElement('button')
    deleteBtn.textContent = '삭제'
    deleteBtn.addEventListener('click', (event) => {
      liElement.remove()
    })
    
    liElement.appendChild(deleteBtn)
  }
}

const getEventAdd = function() {
  const getBtn = document.querySelector('#get-btn')
  const backendURL = 'http://127.0.0.1:8000/api/v1/articles/'

  getBtn.addEventListener('click', (event) => {
    event.preventDefault()
    axios({
      method: 'GET',
      url: backendURL,
      params: {
        content: 'test'
      },
    }).then((response) => {
      console.log('response = ', response.data)
      const articles = response.data

      articles.forEach((article) => {
        makeListItem(article)
      })


    }).catch((error) => {
      console.log('error = ', error)
    })
  })
}

const postEventAdd = function() {
  const getBtn = document.querySelector('#post-form')
  const backendURL = 'http://127.0.0.1:8000/api/v1/articles/'

  getBtn.addEventListener('submit', (event) => {
    event.preventDefault()
    axios({
      method: 'POST',
      url: backendURL,
      data: {
        title: 'test',
        content: 'test'
      },
    }).then((response) => {
      console.log('response = ', response.data)
      const article = {
        id: response.data.id,
        title: response.data.title,
        content: response.data.content
      }
      console.log(`article = ${article}`)
      makeListItem(article)
    }).catch((error) => {
      console.log('error = ', error)
    })
  })
}