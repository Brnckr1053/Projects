(function() {
    'use strict';
    var MyFunComponent = new Class({
        Extends: Rpm.WebComponent,
        componentName: 'MyFunComponent',
        buildComponentContent: function() {
            this.el = {
                link1: this.buildButton('One'),
                link2: this.buildButton('Two'),
                link3: this.buildButton('Three'),
                info : this.buildInfo(),
            };
            return [
                this.el.link1,
                this.el.link2,
                this.el.link3,
                this.el.info
            ];
        },
        buildButton: function(text) {
            return new Element('button', { text: text });
        },
        buildInfo: function() {
            return new Element('div');
        },
        connectComponentUI: function(){
            this.el.link1.addEvent('click', this.buttonClicked.bind(this));
            this.el.link2.addEvent('click', this.buttonClicked.bind(this));
            this.el.link3.addEvent('click', this.buttonClicked.bind(this));
        },
        buttonClicked: function(event)  {
            event.stop();
            var text =  event.target.get('text');
            this.setText(text);
            this.fireEvent('ButtonClicked', text);
        },
        setText: function(text) {
            this.el.info.set('text', text);
            document.getElementById('new-label').innerText = text;
        }
    });

    window.addEvent('load', function() {
        var funComponent = new MyFunComponent({
            instanceID: 'GlobalFunComponent'
        });
        funComponent.renderInside($('old'));
    });
    
})();