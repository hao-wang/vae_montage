load("bf4b12814bc95f34eeb130127d8438ab.js");
load("93fae755edd261212639eed30afa2ca4.js");
load("9943750f07ea537be5f5aa14a5f7b1b7.js");
// Copyright 2009 the Sputnik authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
info: The Object.prototype.toString.length property has the attribute ReadOnly
es5id: 15.2.4.2_A10
description: >
    Checking if varying the Object.prototype.toString.length property
    fails
includes: [propertyHelper.js]
---*/

//CHECK#1
if (!(Object.prototype.toString.hasOwnProperty('length'))) {
  $ERROR('#1: the Object.prototype.toString has length property.');
}

var obj = Object.prototype.toString.length;

verifyNotWritable(Object.prototype.toString, "length", null, function(){return "shifted";});

//CHECK#2
if (Object.prototype.toString.length !== obj) {
  $ERROR('#2: the Object.prototype.toString length property has the attributes ReadOnly.');
}
