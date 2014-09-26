/* mezzanine image block */
  SirTrevor.Blocks.Mezzimage = (function(){
    var template = _.template([
	  '<div  class="img-meta-container">',
      '<input maxlength="140" name="width" placeholder="Image width"',
      ' class="st-input-string js-width-input" type="text" />',
	  '<input maxlength="140" name="height" placeholder="Image height"',
      ' class="st-input-string js-height-input" type="text" />',
	  '<select name="align" class="js-align-input">',
	  '<option value="">Position</option>',
	  '<option value="left">Left</option>',
	  '<option value="center">Center</option>',
	  '<option value="right">Right</option>',
	  '</select>',
      '</div>',
	  '<div class="img-block-container">',
	  '<img class="img">',
	  '</div>'
    ].join("\n"));
  
    
	return SirTrevor.Blocks.Image.extend({
  
    type: "mezzimage",
    editorHTML: function() {
        return template(this);
      },
    loadData: function(data){
      
	  this.$('.img').attr('src',data.file.url).attr('width',data.width).attr('height',data.height);
	  this.$('.js-width-input').val(data.width);
	  this.$('.js-height-input').val(data.height);
	  this.$('.js-align-input').val(data.align);
	  this.$('.img-block-container').css('text-align',data.align);
	  
    },
	  
    onBlockRender: function(){
	  	var that =  this;
        var dt = that.getData();
       this.$inputs.find('button').prev().remove();
       this.$inputs.find('button').bind('click', function(ev){ 
	     ev.preventDefault();
		      		 
		 var ur = mediaLibrary.open(function(url) {
			if (url) {
		      var data = new FormData();
			var obj = {
					  file: {
						url: url,
					}
              } 
             that.setAndLoadData(obj);
             that.ready();
			  
			 // that.$inputs.hide();
             // that.$editor.html($('<img>', { src: url })).show();
			  
			  
        
			}
		}, 'image');
		 
	  });
         this.$inputs.find('input').on('change', _.bind(function(ev){
        this.onDrop(ev.currentTarget);
      }, this));
    },
     
  });
 })();