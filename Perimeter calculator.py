var choice = prompt("Welcome to Area Calculator. \n Please Enter your choice.\n1.Area of Rectangle. \n2.Area of Triangle. \n3.Area of Circle. \n4.Area of parellelogram");

if (choice == '1') {
    var l =prompt('Enter length')
    var b = prompt('Enter the breadth')
    var result = Number(1) * Number(b)
    alert('The Area is ' + result)
}


if (choice == '2') {
    var h =prompt('Enter height')
    var b = prompt('Enter the base')
    var result = Number(h) * Number(b) / 2
    alert('The Area is ' + result)
}

if (choice == '3') {
    var r =prompt('Enter the radius')
    var result = 3.14 * Number(h) * Number(r)
    alert('The Area is ' + result)
}