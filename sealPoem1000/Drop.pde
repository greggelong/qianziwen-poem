class Drop {
  float x, y;
  float speed;
  color c;
  float r;
  String [] poem = {"名", "几", "后", "月", "的", "和", "生", "东", "字", "大", "回", "见", "水", "听", "友", "下", "少", "八", "会", "日", "女", "钟", "想", "好", "有", "天", "菜", "年", "车", "都", "老", "高", "作", "气", "儿", "一", "再", "去", "谁", "说", "明", "服", "衣", "京", "出", "雨", "谢", "读", "语", "饭", "爱", "西", "子", "面", "欢", "在", "热", "能", "飞", "不", "习", "多", "人", "中", "机", "是", "火", "起", "上", "坐", "时", "二", "书", "兴", "学", "岁", "写", "杯", "我", "工", "师", "分", "来", "五", "九", "四", "同", "星", "汉", "国", "果", "对", "家", "本"};
  String [] ppoem = {"name","some","after","moon","of","and","born","east","word","big","return","see","water","hear","friend","below","few","eight","metting","sun","woman","clock","think","good","have","sky","vegetables","year","car","capital","old","tall","work","air","child","one","again","go","who","speak","bright","clothes","garment","east","go out","rain","thank","read","language","meal","love","west","son","face","joyous","exist","heat","ability","fly","not","study","more","man","middle","machine","be","fire","rise","up","sit","time","two","book","light","knowledge","age","write","cup","I","labor","teacher","part", "arrive","five", "nine", "four", "alike", "star", "man","country","fruit", "answer","family","root"}; 
  float size;
  int poemIdx;
  
  

  Drop() {
    r= 8;
    x= random(width);
    y= -r*4;
    speed = random(1, 5);
    c= color(0, 0, 0);
    size = random(40,120);
    poemIdx =int(random(poem.length));
  }

  void move() {
    y += speed;
  }
  
  void caught(){
    fill(color(255,0,0));
    textFont(g,size);
    text(ppoem[poemIdx],x,y-size);
    text(poem[poemIdx],x+size, y);
    speed =0;  // no speed and off the screen
    //y = -1000;
    
  }

  boolean reachedBottom() {
    if (y> height+ r*4) {
      y=-1000;  // needed to get the y value not to reach bottom more than onece
      speed = 0;
      return true;
      
      
    } else {
      return false;
    }
  }

  void display() {
    fill(c);
    noStroke();
    textFont(f,size);
    text(poem[poemIdx],x, y);
    }
  }
