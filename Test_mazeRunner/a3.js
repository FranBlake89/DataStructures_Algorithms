var theMaze;
var pathFileInput;
var pathFile;
var radio;
var thePath;
var theCanvas;
var cellWidth;
var theLegend;
function Maze(){
	that={};
	var width_;
	var height_;
	var walls_;
	var initialized_=false;
	var cellWidth_;
	var start_;
	var end_;
	var flashFrame_;
	that.init = function(obj){
		mazeData=JSON.parse(obj);
		width_=mazeData.maxCol;
		height_=mazeData.maxRow;
		walls_=mazeData.walls;
		wallWidth_=5;
		initialized_=true;
		cellWidth_=min(int(1000/width_),20);
		cellWidth=cellWidth_;
		start_=mazeData.start;
		end_=mazeData.end;
		flashFrame_=0;
	}
	that.getRow=function(cell){
		return cell/height_;
	}
	that.getCol=function(cell){
		return cell%width_;
	}
	that.draw=function(){
		if(initialized_){
			strokeWeight(5);
			line(0,2.5,(width_*cellWidth_)+9,2.5);
			line(0,(height_*cellWidth_)+8,(width_*cellWidth_)+9,(height_*cellWidth_)+8);
			line(2.5,0,2.5,(height_*cellWidth_)+8);
			line((width_*cellWidth_)+9,0,(width_*cellWidth_)+9,(height_*cellWidth_)+8);

			strokeWeight(1);
			for(var i=0;i<walls_.length; i++){
				cell1=walls_[i][0];
				cell2=walls_[i][1];
				if(cell1 > cell2){
					var tmp=cell1;
					cell1=cell2;
					cell2=tmp;					
				}
				r1=int(cell1/width_);
				c1=cell1%width_;
				r2=int(cell2/width_);
				c2=cell2%width_;
				if(r1==r2){
					line(5+(c2*cellWidth_),5+(r1*cellWidth_), 5+(c2*cellWidth_),5+((r1+1)*cellWidth_));
				}
				else{
					line(5+(c2*cellWidth_),5+(r2*cellWidth_), 5+((c2+1)*cellWidth_),5+(r2*cellWidth_));					
				}
			}

		}
		push();
		var r;
		var c;
		if(flashFrame_< 30){
			stroke(0,0,255);
			fill(0,0,255);
			r=int(start_/width_);
			c=start_%width_;
			rect(7+c*cellWidth_,7+r*cellWidth_,(cellWidth_-4),(cellWidth_-4));

			stroke(0,255,0);
			fill(0,255,0);
			r=int(end_/width_);
			c=end_%width_;
			rect(7+c*cellWidth_,7+r*cellWidth_,(cellWidth_-4),(cellWidth_-4));
		}
		else{
			stroke(0,255,0);
			fill(0,255,0);
			r=int(end_/width_);
			c=end_%width_;
			rect(7+c*cellWidth_,7+r*cellWidth_,(cellWidth_-4),(cellWidth_-4));


			stroke(0,0,255);
			fill(0,0,255);
			r=int(start_/width_);
			c=start_%width_;
			rect(7+c*cellWidth_,7+r*cellWidth_,(cellWidth_-4),(cellWidth_-4));

		}
	if(flashFrame_!=60){
			flashFrame_++;
		}
		else{
			flashFrame_=0;
		}
		pop();
	}
	that.mazeWidth=function(){
		return width_;
	}
	that.mazeHeight=function(){
		return height_;
	}
	that.cellWidth=function(){
		return cellWidth_;
	}
	that.isInitialized=function(){
		return initialized_;
	}
	that.reset=function(){
		initialized_=false;
	}
	return that;
}


function Path(){
	var that = {};
	var initialized_=false;
	var path_;
	var pathLength_;
	var rows_;
	var cols_;

	var curr_=0;
	var frameCount_=0;
	that.init=function(pathArray){
		pathData=JSON.parse(pathArray);
		path_=pathData.path;
		pathLength_=pathData.pathLength;

		rows_=pathData.rows;
		cols_=pathData.cols;
		initialized_=true;
		frameCount_=0;
	}


	that.drawPath=function(){
		if(initialized_){
			push();
			if(pathLength_ > 1){
				for(var i=0;i<curr_;i++){
					fill(255,0,0);
					stroke(255,0,0);
					strokeWeight(3);
					var r1=int(path_[i]/cols_);
					var c1=path_[i]%cols_;
					var r2=int(path_[i+1]/cols_);
					var c2=path_[i+1]%cols_;
					line((c1*theMaze.cellWidth()) + theMaze.cellWidth()/2 + 5,(r1*theMaze.cellWidth())+theMaze.cellWidth()/2 + 5,(c2*theMaze.cellWidth())+theMaze.cellWidth()/2 + 5,(r2*theMaze.cellWidth())+theMaze.cellWidth()/2 + 5);
				}
			}
			else if (pathLength_ == 1){
				fill(255,0,0);
				stroke(255,0,0);
				strokeWeight(3);
				var r1=int(path_[0]/cols_);
				var c1=path_[0]%cols_;
				ellipse (c1*theMaze.cellWidth() + theMaze.cellWidth()/2 + 5,(r1*theMaze.cellWidth())+theMaze.cellWidth()/2 + 5,3,3);
			}
			frameCount_++;
			if(frameCount_ ==5){
				if(curr_ < pathLength_-1){
					curr_+=1
				}
				else{
					noLoop()
				}
				frameCount_=0;
			}
			pop();
		}

	}
	that.isInitialized=function(){
		return initialized_;
	}
	that.reset=function(){
		initialized_=false;
		curr_=0;
	}
	return that;
}
function Legend(){
	var that={};
	that.draw=function(){
		var offset=theMaze.mazeHeight()*theMaze.cellWidth()+20;
		push();
		strokeWeight(1);
		stroke(0,0,255);
		fill(0,0,255);
		rect(5,offset,theMaze.cellWidth()-4,theMaze.cellWidth()-4);
		stroke(0);
		fill(0);
		text("start",theMaze.cellWidth()+10,offset+2+theMaze.cellWidth()/2);
		stroke(0,255,0);
		fill(0,255,0);
		rect(90,offset,theMaze.cellWidth()-4,theMaze.cellWidth()-4);
		stroke(0);
		fill(0);
		text("end",theMaze.cellWidth()+95,offset+2+theMaze.cellWidth()/2);
		stroke(0);
		fill(0);
		text("your Path",theMaze.cellWidth()+185,offset+2+theMaze.cellWidth()/2);
		stroke(255,0,0);
		fill(255,0,0);
		strokeWeight(3);
		line(180,offset+theMaze.cellWidth()/2,180+theMaze.cellWidth(),offset+theMaze.cellWidth()/2);
		stroke(0);
		fill(0);



		pop();
	}
	return that;
}
function loadPathFile(file){
	if(thePath.isInitialized()){
		thePath.reset();
	}
	thePath.init(file.data);
}


function loadMazeFile(file){
	if(theMaze.isInitialized()){
		theMaze.reset();
	}
	theMaze.init(file.data);

}

function setup(){
	theMaze=Maze();
	thePath=Path();
	mazeFilePrompt =createP("Load Maze File: ", 10, 5)
	mazeFileInput=createFileInput(loadMazeFile);
	mazeFileInput.position(150,5);
	pathFilePrompt = createP("Load Path File: ", 10, 40)
	pathFileInput=createFileInput(loadPathFile);
	pathFileInput.position(150,40);

	theCanvas=createCanvas(1200,1010);
	theCanvas.position(50,100);
	theLegend=Legend();
}

function draw(){
	background(255,255,255);
	theMaze.draw();
	thePath.drawPath();
	theLegend.draw();
}
