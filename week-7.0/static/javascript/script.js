let nameSearchInput = document.querySelector("#name-search-input")
const nameSearchBtn = document.querySelector("#name-search-btn")

// Week7 Added: Searching for specific user's name
nameSearchBtn.addEventListener("click", (event)=>{
  event.preventDefault();
  let url = "http://127.0.0.1:3000/api/member?username="
  let nameInputValue = nameSearchInput.value

  fetch(url + nameInputValue)
  .then(response => {
    return response.json();})
  .then(response => {
    let usersName = response.data
    let nameSearchResult = document.querySelector("#name-search-result")
    
    if (usersName !== null){
      nameSearchResult.innerHTML = `<div>${usersName.name} (${usersName.username})</div>`
    } else {
      nameSearchResult.innerHTML = `<div>找不到${nameInputValue}</div>`
    }
  })
  document.querySelector("#name-search-input").value = ""
})


// Week7 Added: Changing/updating user's name
let nameEditInput = document.querySelector("#edit-name-input")
let memberContent = document.querySelector(".member-content")
const nameEditBtn = document.querySelector("#edit-name-btn")

nameEditBtn.addEventListener("click", (event)=>{
  event.preventDefault();
  let url = "http://127.0.0.1:3000/api/member?username="
  let nameEditInputValue = nameEditInput.value

  fetch(url + nameEditInputValue, {
    method: "PATCH",
    headers: {"Content-Type": "application/json"},
    body: {"name": nameEditInput}})
  .then(response => {
    return response.json();})
  .then(response => {
    let nameEditResult = document.querySelector("#edit-name-result")
    if (response["ok"]== true){
      nameEditResult.innerHTML = `<div>更新成功</div>`
      memberContent.innerHTML = `${ nameEditInputValue }！歡迎登入系統！`
    } else {
      nameEditResult.innerHTML =`<div>更新失敗／請不要空白</div>`
    }
  })
  document.querySelector("#edit-name-input").value = ""
})