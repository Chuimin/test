<template>
  <div id="about">
    <div id="top">
      <p>todos</p>
    </div>
    <div id="bd">
        <input type="text" id="put" placeholder="What needs to be done ?  " @keyup.enter="addtext" v-model="text">
        <ul class="list">
          <li v-for="item in todolist" v-bind:key="item.id">
            <div class="view">
              <input type="checkbox" name="status" id="status" @click="change('status',item.id)">
              <label id="text">{{item.text}}</label>
              <button class="del" @click="change('del',item.id)">×</button>
            </div>
          </li>
          <li v-if="st">
            <label style="margin-left:0px;">{{num}} items left</label>
            <button>All</button>
            <button>Active</button>
            <button>Completed</button>
            <a @click="change('clean',0)">clear completed</a>
          </li>
        </ul>
    </div>
    <div id="foot">
        <p>Double-click to edit a todo</p>
        <p>Written by <a href="http://evanyou.me">Evan You</a></p>
        <p>Part of <a href="http://todomvc.com">TodoMVC</a></p>
    </div>
  </div>
</template>

<script>

export default {
  data: function () {
    return {
      num: 0,
      text: '',
      st: false,
      todolist: []
    }
  },
  methods: {
    addtext: function () {
      this.todolist.push({
        id: this.num++,
        text: this.text,
        status: false
      })
      this.st = true
      this.text = ''
    },
    change: function (t, id) {
      for (var i = 0; i < this.todolist.length; i++) {
        var id1 = this.todolist[i].id
        if (t === 'clean') {
          console.log(i)
          console.log(this.todolist[i].status)
          if (this.todolist[i].status === true) {
            this.todolist.splice(i, 1)
            i -= 1
          }
          if (this.todolist.length === 0) {
            this.st = false
          }
        }
        if (id1 === id) {
          if (t === 'del') {
            this.todolist.splice(i, 1)
            this.num -= 1
            if (this.todolist.length === 0) {
              this.st = false
            }
          } else if (t === 'status') {
            console.log(this.todolist[i].status)
            this.todolist[i].status = !this.todolist[i].status
            if (this.todolist[i].status === true) {
              this.num -= 1
            } else {
              this.num += 1
            }
            console.log(this.todolist[i].status)
          }
        }
      }
    }
  }
}
</script>

<style lang="scss">
#about{
    height: auto;
    width: 800px;
    border: 1px solid black;
    text-align: center;
    margin: 0 auto;
    margin-top: 100px;
}
#top{
    font-family: "Arial";
    font-size: 120px;
    color: rgb(197, 133, 153);
    font-stretch: ultra-condensed;
}
#top p{
    margin-top: 50px;
    opacity: 0.3;
}
#bd{
    height: auto;
    margin-top: -100px;
}
#bd  #put{
    height: 70px;
    width: 700px;
    font-size: 40px;
    border: 2px solid #a3abb1;
    color: rgb(212, 207, 207);
    box-shadow: 0 25px 35px #d5d6d8;

}
#bd  #put::-webkit-input-placeholder{
    color: rgb(212, 207, 207);
}
#foot{
    margin-top: 100px;
}
#foot p{
    color: darkgray;
}
#foot p a{
    text-decoration: none;
    color: darkgray;
}
#foot p a:hover{
    text-decoration: underline ;
}

#bd ul li{
    list-style: none;
}
#bd ul li .view{
    text-align: left;
    height: 70px;
    width: 705px;
    margin-left: 8px;
    margin-top: -15px;
}
#bd ul li .view #text{
    width: 600px;
    height: 50px;
    font-size: 40px;
    display:inline-block;
    // text-decoration: line-through;
}
#bd ul li .view #status{
    height: 50px;
    width: 50px;
    margin-left: 0px;
    border-radius:50px;
    margin-top: 5px;
    font-weight: 100;
    display: inline-block;
}
#bd ul li .view .del {
    height: 50px;
    width: 50px;
    font-size: 30px;
    margin-right: 0px;
    background: white;
    border: 1px solid white;
    color: rgb(197, 91, 91);
    display: inline-block;
    top: -16px;
}
#bd ul li .view .del:hover{
    color: rgb(179, 78, 78);
}
</style>
