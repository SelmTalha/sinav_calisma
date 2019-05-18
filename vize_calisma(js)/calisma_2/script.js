let str="Gözde";
let str2=" ";
for (let i=str.length-1;i>=0;i--){
    str2=str2+str[i]
}
alert(str2)
var a="Ali'nin atı";
console.log(a);
// var b=a.substring(1)
// console.log(b);
let b=a.substring(1,a.indexOf(" "));
console.log(b);
console.log(b.length);