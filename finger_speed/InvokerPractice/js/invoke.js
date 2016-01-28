var sectionIDs = ['practice', 'baseline', 'training', 'posttest', 'download'];
var sections = [practice, baseline, training, posttest, downloadJson];
var taskNum = 0;
var bio;

function submitForm() {
    var email = $('#email').val();
    var age = $('#age').val();
    var gender = $('#gender').val();
    var rank = $('#mmr').val();
    var exp = $('#exp').val();
    var data = {
        'email': email,
        'age': age,
        'gender': gender,
        'rank': rank,
        'exp': exp,
    }
    bio = data;
    addToResponseData((new Date()).getTime().toString(), 'bio', data);
    $('#btnSubmit').css('display', 'none');
    $('#bioForm').css('display', 'none');
    $('#btnpractice').css('display', 'block');
}

function practice() {
    var combosToDo = ['3', '9', '8', '1'];
    $('#btnpractice').css('display', 'none');
    initialize('practice', combosToDo);
    taskNum++;
}

function baseline() {
    var combosToDo = ['3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1', '3', '9', '8', '1'];
    $('#btnbaseline').css('display', 'none');
    initialize('baseline', combosToDo);
    taskNum++;
}

function training() {
    var combosToDo = ['1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3', '1', '9', '8', '3'];
    $('#btntraining').css('display', 'none');
    initialize('training', combosToDo);
    taskNum++;
}

function posttest() {
    var combosToDo = ['9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8', '9', '1', '3', '8'];
    $('#btnposttest').css('display', 'none');
    initialize('posttest', combosToDo);
    taskNum++;
}

function downloadJson() {
    $('#doneInstructions').css('display', 'block');
}

function Circle(color, letter, url) {
    this.color = color;
    this.letter = letter;
}

function updateCircles() {
    _.each(queue, function(circle, i) {
        $('#' + queueIds[i]).css('background-image', circle.color);
        $('#' + queueIds[i]).text(circle.letter);
    })
}

var queueIds = ['circleOne', 'circleTwo', 'circleThree', 'circleFour', 'circleFive', 'circleSix'];
var queueKeys = ['1', 'q', 'w', 'e', 'r', 'd'];

function initialize(mode, combosToDo) {
    //queue = _.map(queueKeys, function(key) {return new Circle('#FFFFFF', '')});
    queue = _.map(queueKeys, function(key) {return new Circle('https://upload.wikimedia.org/wikipedia/commons/d/d2/Solid_white.png', '')});
    updateCircles();
    $(document).unbind('keydown')
    $(document).unbind('keyup')
    $(document).on('keydown', function(event){
		var keyCode = (event.keyCode ? event.keyCode : event.which);
        execute(keyCode);
    });
    $(document).on('keyup', function(event){
        var keyCode = (event.keyCode ? event.keyCode : event.which);
        addToResponseData((new Date).getTime().toString(), 'key up', {})
    })
    var data = {
        'task mode': mode,
        'combos': combosToDo,
    }
    addToResponseData((new Date).getTime().toString(), 'initialize', data);
    comboList = combosToDo.slice(0);
	comboNumber = comboList.shift();
	console.log("Your first combo is");
	console.log(combos[comboNumber].sequence);
	indicateNextCombo(combos[comboNumber].sequence.toUpperCase());
	showNextComboImage();
	console.log("Game begun");
}

function configureFingers(name, key) {
    var response = prompt("Please enter what key you want for " + name, String.fromCharCode(key))
    var value = defaultFingerMapping[key]
    delete defaultFingerMapping[key]
    defaultFingerMapping[response.charCodeAt(0) - (!$.isNumeric(response) * 32)] = value;
}

//var defaultFingerMapping = {68: 5, 49: 9, 81: 1, 87: 2, 69: 3, 82: 4}
var defaultFingerMapping = {68: 'd', 49: '1', 81: 'q', 87: 'w', 69: 'e', 82: 'r'}
var colorMapping = {'d': 'url("http://hydra-media.cursecdn.com/dota2.gamepedia.com/3/39/Invoker.png?version=cc2a440da5178b1ebbf2778cba02b9b2")', '1': 'url("http://i.imgur.com/y7BAZmz.png")', 'q': 'url("http://i.imgur.com/4VlAp5E.png")', 'w': 'url("http://i.imgur.com/Y6Dvgnn.png")', 'e': 'url("http://i.imgur.com/volAeD9.png")', 'r': 'url("http://i.imgur.com/gJ4etuO.png")'}
// Your color history
var queue;
// need function to assign new finger mappings

var combos = [
	{
	"name": "coldsnap",
	"color": "#3366FF",
    "sequence": "1qqqrd",
	"image": 'url("http://i.imgur.com/JTlUPwY.png")',
	},
	{
	"name": "ghostwalk",
	"color": "#6633FF",
    "sequence": "1qqwrd",
	"image": 'url("http://i.imgur.com/oQS5lTU.png")',
	},
	{
	"name": "icewall",
	"color": "#FF33CC",
    "sequence": "1qqerd",
	"image": 'url("http://i.imgur.com/e2L27wh.png")',
	},
	{
	"name": "emp",
	"color": "#33CCFF",
    "sequence": "1wwwrd",
	"image": 'url("http://i.imgur.com/sHvsDqL.png")',
	},
	{
	"name": "tornado",
	"color": "#FF3366",
    "sequence": "1qwwrd",
	"image": 'url("http://i.imgur.com/e0Yq9Hg.png")',
	},
	{
	"name": "alacrity",
	"color": "#003DF5",
    "sequence": "1wwerd",
	"image": 'url("http://i.imgur.com/XgALJpp.png")',
	},
	{
	"name": "sunstrike",
	"color": "#CC2B14",
    "sequence": "1eeerd",
	"image": 'url("http://i.imgur.com/ltGo5OL.png")',
	},
	{
	"name": "forgespirit",
	"color": "#CC33FF",
    "sequence": "1qeerd",
	"image": 'url("http://i.imgur.com/JTlUPwY.png")',
	},
	{
	"name": "chaosmeteor",
	"color": "#FF668C",
    "sequence": "1weerd",
	"image": 'url("http://i.imgur.com/sd52hs3.png")',
	},
	{
	"name": "deafeningblast",
	"color": "#D9FF66",
    "sequence": "1qwerd",
	"image": 'url("http://i.imgur.com/IfcQLSF.png")',
	},
];

// This is the list of 10 combo integers that we will use for the challenge
var comboList = new Array();

var comboNumber;
var responseData = {};

function addToResponseData(timestamp, state, data) {
    responseData[timestamp] = {
        'state': state,
        'data': data,
    }
}

// Number of presses
var presses = 0;


function addToQueue(color, letter){
	queue.shift();
	queue.push(new Circle(color, letter));
    updateCircles();
}


// Array shuffler
function shuffle(o){
    for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
}


function execute(keyCode){
    var timestamp = (new Date).getTime().toString();
    var targetQueue = combos[comboNumber].sequence;
    var successState = 'unmatched';
    if (keyCode in defaultFingerMapping) {
        addToQueue(colorMapping[defaultFingerMapping[keyCode]], defaultFingerMapping[keyCode])
        var currentQueue = _.map(queue, function(q) {return q.letter}).join('');
        console.log(targetQueue);
        console.log(currentQueue);
        if (targetQueue == currentQueue) {
            successState = 'matched';
			flashStatus();
            if (comboList.length > 0) {
                comboNumber = comboList.shift();
                console.log("Your next combo is");
			    showNextComboImage();
                console.log(combos[comboNumber].sequence);
				indicateNextCombo(combos[comboNumber].sequence.toUpperCase());
                queue = _.map(queueKeys, function(key) {return new Circle('', '')});
                updateCircles();
            } else {
                endGame(taskNum);
            }
        }
		else {
			resetStatus();
		}
    }
    var data = {
        'key event': keyCode,
        'target queue': targetQueue,
        'current queue': currentQueue,
        'success state': successState,
    };
    addToResponseData(timestamp, 'key down', data);
}

function endGame(nextTask){
    $(document).unbind('keydown')
    $(document).unbind('keyup')
    queue = _.map(queueKeys, function(key) {return new Circle('', '')});
    updateCircles();
    $('#nextComboName').text('');
    $('#nextCombo').text('');
    clearComboImage();
    $('#btn' + sectionIDs[taskNum]).css('display', 'block')
    if (taskNum == sectionIDs.length - 1) {
        $('#btndownload').html('<a href="data:' + encodeURI("text/json;charset=utf-8," + JSON.stringify(responseData)) + '" download="' + bio['email'].replace('@', '_').replace('.', '_') + '.json">Download Json</a>');
    }
}

function showHideMenuClick(){
	if ($('#cheatsheet').css('display') == 'block') {
        $('#cheatsheet').css('display', 'none');
        $('#btnShowHide').text('Show Cheat Sheet');
    }
    else {
        $('#cheatsheet').css('display', 'block');
        $('#btnShowHide').text('Hide Cheat Sheet');
    }
}

function showHideMenuClick1(){
	if ($('#thisInfo').css('display') == 'block') {
        $('#thisInfo').css('display', 'none');
        $('#btnShowHide1').text('Show FAQ');
    }
    else {
        $('#thisInfo').css('display', 'block');
        $('#btnShowHide1').text('Hide FAQ');
    }
}

function flashStatus(){
	$("#status").fadeOut(100, function() {
		$(this).css('color', '#00CC66');
		$(this).text("Status: Correct").fadeIn(100);
	});
}

function resetStatus(){
	$("#status").css('color', '#FF0000');
	$("#status").text("Status: Incorrect");
}

function indicateNextCombo(s){
	var a = s.split('').join(' ');
	$("#nextCombo").fadeOut(0, function() {
		$(this).text(a).fadeIn(0);
	});
	
	$("#nextComboName").fadeOut(0, function() {
		$(this).text(combos[comboNumber].name.toUpperCase()).fadeIn(0);
	});	
}

function showNextComboImage(){
	console.log(combos[comboNumber].image);
	$('#skillPic').css('background-image', combos[comboNumber].image);
	$('#skillPic').css('display', 'block');
}

function clearComboImage() {
    $('#skillPic').css('background-image', '');
}
