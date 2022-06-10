Rpm = {};

(function () {
	'use strict';

	Rpm.WebComponent = new Class({
		Implements: [Options, Events],
		options: {
			instanceID: ''
		},
		componentName: 'WebComponent',
		container: null,
		content: null,
		// You usually don't need to extend renderInside directly, see:
		// - buildComponentContent
		// - connectComponentUI
		renderInside: function (container) {
			this.container = container;
			this.reRender();
		},
		reRender: function () {
			if (this.content === null) {
				this.render();
			}

			this.container
				.empty()
				.adopt(this.content)
				.addClass(this.componentName + '--container');
			this.connectComponentUI();
			this.addIDToElement(this.container, 'Container');
			// Store this component in the container
			this.container.store('WebComponent', this);
		},
		render: function () {
			this.content = this.buildComponentContent();
		}.protect(),
		/*
			Build and return a list of DOM elements that make
			up the Component's UI.
		*/
		buildComponentContent: function () {
			return new Element('span', { 'html': 'Rpm.WebComponent (' + this.templateNamespace + ')' });
		},
		addIDToElement: function (el, id) {
			if (this.options.instanceID === '') {
				return;
			}
			el.set('id', this.buildID(id));
		},
		buildID: function (id) {
			return this.options.instanceID + ':' + id;
		},

		/*
			Connect the UI element's events, usually this means 
			eventually firing one of the Component's events.
		*/
		connectComponentUI: function () { },

	});
	
})();