class Load{
    constructor(local){
        this.local = local;
        this.load = document.createElement('div')
        this.load.className = 'load'
        this.load.status = 'parado'        
    }

    get criar(){
        this.local.append(this.load)
    }
}

export default Load