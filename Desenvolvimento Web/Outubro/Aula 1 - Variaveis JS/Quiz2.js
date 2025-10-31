const priceRose = 8
let quantRoses = 70

const priceLilly = 10
let quantLillies = 50

const priceTulip = 2 
let quantTullip = 120

quantRoses -= 20
quantLillies -= 30

let totalPriceRoses = priceRose * quantRoses
let totalPriceLillies = priceLilly * quantLillies
let totalPriceTullips = priceTulip * quantTullip
 
let totalPrice = totalPriceRoses + totalPriceLillies + totalPriceTullips

console.log("priceRose – unit price:", priceRose,", quantity:", quantRoses, ", value:", totalPriceRoses)
console.log("priceLilly – unit price:", priceLilly,", quantity:", quantLillies, ", value:", totalPriceLillies)
console.log("priceTulip – unit price:", priceTulip,", quantity:", quantTullip, ", value:", totalPriceTullips)
console.log("Total:", totalPrice)