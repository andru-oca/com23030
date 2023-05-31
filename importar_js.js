async function getJson(){
    const res = await fetch("data.json")
    const datos = await res.json()
    console.log(datos)
} 