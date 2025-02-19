class Get_requisição{
    constructor(url,filter){
        this.url = url;
        this.filter = '/?'
        for(var f = 0 ;f <filter.length;f++){
            if(f == filter.length - 1){
                this.filter += `${filter[f]}`
            }else{
                this.filter += `${filter[f]}&`
            }
        }
    }

    async result(){
        this.url_req = `${this.url}${this.filter}`
        try{
            let fetch_var = await fetch(this.url_req)
            let fetch_var_json = fetch_var.json()
            return fetch_var_json
        }
        catch(e){
            console.log(e)
        }
    }
}


export default Get_requisição