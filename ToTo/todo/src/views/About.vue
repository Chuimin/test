<template>
  <div id="about">
    <div id="top">
      <p>todos</p>
    </div>
    <div id="bd">
        <input type="text" id="put" placeholder="What needs to be done ?  " @keyup.enter="addtext" v-model="text">
        <input type="checkbox" class="all" v-show="false">
        <label for="all"></label>
        <ul class="list">
          <li v-for="item in todolist" v-bind:key="item.id" v-show="todolist.length">
            <div class="view">
              <!-- v-bind:style="item.labsty" -->
              <input type="checkbox" :class="item.classname" v-bind:id="item.id" v-show="false" >
              <label v-bind:for="item.id" @click="change('status',item.id)"></label>
              <label type="text" class="text" v-bind:style="item.sty" @dblclick="look2(item.id)">{{item.text}}</label>
              <button class="del" @click="change('del',item.id)">×</button>
            </div>
          </li>
          <li v-if="st" class="fd">
            <label class="items" style="margin-left: -200px;">{{num}} items left</label>
            <button @click="show('all')"  style="margin-left: 100px;background: #f2f7fa;border: 1px solid #f2f7fa;">All</button>
            <button @click="show('active')" style="margin-left: 10px;background: #f2f7fa;border: 1px solid #f2f7fa;">Active</button>
            <button @click="show('completed')" style="margin-left: 10px;background: #f2f7fa;border: 1px solid #f2f7fa;">Completed</button>
            <a @click="change('clean',0)" v-if="stam()" style="margin-right: -200px;margin-left: 100px;">clear completed</a>
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
      todo: [],
      todolist: []
    }
  },
  methods: {
    addtext: function () {
      if (this.text === '') {
        alert('不能输入空')
        return
      }
      this.todolist.push({
        classname: 'status',
        id: this.num++,
        text: this.text,
        status: false,
        sty: ''
      })
      this.todo = this.todolist.slice()
      this.st = true
      this.text = ''
    },
    change: function (t, id) {
      for (var i = 0; i < this.todolist.length; i++) {
        var id1 = this.todolist[i].id
        if (t === 'clean') {
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
            console.log(this.todolist[i].classname)
            this.todolist[i].status = !this.todolist[i].status
            if (this.todolist[i].status === true) {
              this.num -= 1
              this.todolist[i].classname = 'status1'
              this.todolist[i].sty = 'text-decoration: line-through ; color: rgb(212, 207, 207) ; font-style: oblique ;'
            } else {
              this.num += 1
              this.todolist[i].sty = ''
              this.todolist[i].classname = 'status'
            }
            console.log(this.todolist[i].classname)
          }
        }
      }
      this.todo = this.todolist.slice()
    },
    mode: function (id) {
      console(this.todolist[id].status)
    },
    look2: function (id) {

    },
    show: function (t) {
      this.todolist.splice(0, this.todolist.length)
      for (var i = 0; i < this.todo.length; i++) {
        if (t === 'all') {
          this.todolist.push(this.todo[i])
        } else if (t === 'active') {
          if (this.todo[i].status === false) {
            this.todolist.push(this.todo[i])
          }
        } else if (t === 'completed') {
          if (this.todo[i].status === true) {
            this.todolist.push(this.todo[i])
          }
        }
      }
    },
    stam: function () {
      var m = 0
      for (var i = 0; i < this.todolist.length; i++) {
        if (this.todolist[i].status === true) {
          m = 1
        }
      }
      return m
    }
  }
}
</script>

<style lang="scss">
#about{
    height: 600px;
    width: 800px;
    text-align: center;
    margin: 0 auto;
    margin-top: 100px;
    overflow:scroll;
    background: #f2f7fa;
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
    width: 700px;
    margin-top: -200px;
    margin: auto;
    box-shadow: 0 25px 35px #d5d6d8;
    margin-top: -60px;
}
#bd  #put{
    height: 70px;
    width: 700px;
    font-size: 40px;
    border: 2px solid #a3abb1;
    color: rgb(212, 207, 207);
}
#bd  #put::-webkit-input-placeholder{
    color: rgb(212, 207, 207);
}
.all + label {
    display: inline-block;
    border: 1px solid black;
    width: 60px;
    height: 34px;
    font-size: 20px;
    position: absolute;
    top: -52px;
    left: -13px;
}
.all + label:before{
    content: '❯';
    font-size: 22px;
    color: #e6e6e6;
    padding: 10px 27px 10px 27px;
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
    margin-left: -30px;
}
#bd ul li .view{
    text-align: left;
    height: 70px;
    width: 705px;
    margin-top: -15px;
}
#bd ul li .view .text{
    width: 590px;
    height: 50px;
    font-size: 30px;
    font-family: "仿宋";
    display:inline-block;
    border: 1px solid #f2f7fa;
}
#bd ul li .view .status{
  display: inline-block;
}
.status + label{
    background-color: #f2f7fa;
    border-radius: 30px;
    border:1px solid #d3d3d3;
    width:40px;
    height:40px;
    display: inline-block;
    text-align: center;
    vertical-align: middle;
    line-height: 20px;
    font-size: 27px;
    margin-top: -8px;
}
.status1 + label{
    background-color: #f2f7fa;
    border-radius: 30px;
    border:1px solid #d3d3d3;
    width:40px;
    height:40px;
    display: inline-block;
    text-align: center;
    vertical-align: middle;
    line-height: 20px;
    font-size: 27px;
    margin-top: -8px;
    background-color: #eee;
}
.status1 + label:before{
  content:"\2714";
}
.status:checked + label{
  background-color: #eee;
}
.status:checked + label:after{
  content:"\2714";
}
#bd ul li .view .del {
    height: 50px;
    width: 50px;
    font-size: 30px;
    margin-right: 0px;
    background: #f2f7fa;
    border: 1px solid #f2f7fa;
    color: rgb(197, 91, 91);
    display: inline-block;
    top: -16px;
}
#bd ul li .view .del:hover{
    color: rgb(179, 78, 78);
}
#bd ul li .fd{
  text-align: left;
}
#bd ul li .fd label.items{
    margin-left: -200px;
    display: block;
}
#bd ul li li.fd button:hover{
  border: 1px solid palevioletred;
}
</style>
