'use strict'

const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

fetch(url).then(function(response){
  return response.json()
}).then(function(data){

  let spotData = data["result"]["results"]

  // add 2 small photos at the top of the page
  for(let i=0; i<2; i++){
    // get URLs of photos
    let photoFiles = spotData[i]["file"].split("https://")
    let photoUrl = "https://" + photoFiles[1]
    // get names of spots
    let spotName = spotData[i]["stitle"]

    addPromotion(photoUrl, spotName)
  }

  // add 8 big photos at the bottom of the page
  for (let i = 2; i < 10; i++){
    // get URLs of photos
    let photoFiles = spotData[i]["file"].split("https://")
    let photoUrl = "https://" + photoFiles[1]
    // get names of spots
    let spotName = spotData[i]["stitle"]
    addBigSpot(photoUrl, spotName)
  }

  // load more button
  const loadMoreBtn = document.querySelector(".load-more-btn")
  let currentIndex = 10
  loadMoreBtn.addEventListener('click', function loadMore() {
    let loadNumbers = 8
    for (let i = currentIndex; i < currentIndex + loadNumbers; i++) {
      if (currentIndex >= spotData.length-loadNumbers){
        loadMoreBtn.style.display="none"
      }
      // get URLs of photos
      let photoFiles = spotData[i]["file"].split("https://")
      let photoUrl = "https://" + photoFiles[1]
      // get names of spots
      let spotName = spotData[i]["stitle"]
      addBigSpot(photoUrl, spotName)
    } 
    currentIndex += loadNumbers
  })

})

// add 2 small photos at the top of the page
function addPromotion(imgLink, caption){
  const promotionBox = document.querySelector(".promotion-box")
  let promotionDiv = document.createElement("div")
  promotionDiv.classList.add("promotion")
  promotionBox.appendChild(promotionDiv)

  let image=document.createElement("img")
  image.src=imgLink
  promotionDiv.appendChild(image)
  
  let promotionCaption = document.createElement("div")
  promotionCaption.textContent= caption
  promotionDiv.appendChild(promotionCaption)
}

// add 8 big photos at the bottom of the page
function addBigSpot(imgLink, caption) {
  const titleItemBox = document.querySelector(".title-item-box")
  let spotDiv = document.createElement("div")
  spotDiv.classList.add("title-item")
  titleItemBox.appendChild(spotDiv)

  let image = document.createElement("img")
  image.src = imgLink
  spotDiv.appendChild(image)

  let spotCaption = document.createElement("div")
  spotCaption.textContent = caption
  spotDiv.appendChild(spotCaption)
}

