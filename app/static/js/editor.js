/**
 * Created by Tran Huu Cuong on 2015-10-28 19:48:00.
 */

var codeArea = $('#code');

var editor = CodeMirror.fromTextArea(codeArea[0], {
    indentUnit: 4,
    lineWrapping: true,
    mode: "markdown",
    theme: "eclipse",
    lineNumbers: "true"
});
