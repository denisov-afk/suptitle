"use strict";


const {EditorState} = require("prosemirror-state")
const {EditorView} = require("prosemirror-view")
const {Schema, DOMParser} = require("prosemirror-model")
const {schema} = require("prosemirror-schema-basic")
const {addListNodes} = require("prosemirror-schema-list")
const {exampleSetup} = require("prosemirror-example-setup")
 
 const wordsJson = '{"words": [{"word": "create", "end_time": 0.5, "start_time": 0.0}, {"word": "an", "end_time": 0.6, "start_time": 0.5}, {"word": "account", "end_time": 0.9, "start_time": 0.6}], "confidence": 0.9354454278945923, "transcript": "create an account", "language_code": "en_us", "sample_rate_hertz": 24000}';
 
 let phrase;
 if(wordsJson){
	 phrase = JSON.parse(wordsJson)
	 };







let state = EditorState.create({schema});
let view = new EditorView(document.querySelector('#home'), {state});
