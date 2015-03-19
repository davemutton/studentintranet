function uniq(a) {
    return a.sort().filter(function(item, pos) {
        return !pos || item != a[pos - 1];
    })
}

function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return("");
}

function RewriteUrlWithTags()
{
        var base_url = window.location.origin;
        
        var tags = uniq(tags_list).join("/")
        var level = uniq(level_list).join("/")
        var age= uniq(agebracket_list).join("/")
        var pathway = uniq(pathway_list).join("/")
        var subject = uniq(subject_list).join("/")
        url = base_url+"/mediamanager/search?tag="+tags+"&level="+level+"&age="+age+"&pathway="+pathway+"&subject="+subject;
        return(url);

}

function DaveSlugify(input_text)
{
var output_text = input_text.replace(/%20/g,"-").replace(/[\.,~%$!\^\*()'{}]+/g,"").replace(" ","-").toLowerCase();
output_text =output_text.replace(" ","-")
console.log(output_text)
return(output_text);




}