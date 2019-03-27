import bpy,re,os;
from bpy_extras.io_utils import ExportHelper;
from bpy.props import StringProperty, BoolProperty, EnumProperty;
from bpy.types import Operator;

CYCLES_EXPORTABLE_MATS_PATTERN=re.compile("\\!\s*([^;]+)");
CYCLES_MAT_INPUT_PATTERN=re.compile("\\!\s*([^;]+)");

FORMAT_EXT={
    "bmp":"bmp",
    "dds":"dds",
    "hdr":"hdr",
    "targa":"tga",
    "jpeg":"jpg",
    "targa_raw":"tga",
    "targa":"tga",
    "png":"png"
};


def findF3bMaterial(intree,filter):
    for  n in intree.nodes:
        print(n)
        if (isinstance(n,bpy.types.ShaderNodeOutputMaterial)):
            if(len(n.inputs[0].links)==0):
                return [None,n];
                
            else:a
                fn=n.inputs[0].links[0].from_node
                if ( isinstance(fn, bpy.types.ShaderNodeGroup )):
                    if(CYCLES_EXPORTABLE_MATS_PATTERN.match(fn.node_tree.name) and (filter==None or filter==fn.node_tree.name)):
                        return [fn,n];                   
                return [None,n];               
    n=intree.nodes.new('ShaderNodeOutput');
    return [None,n];
    



def run(path,mat):
    for  obj in bpy.context.scene.objects:
        if (obj.select):
            for  i in range(0,len(obj.material_slots)):
                material=obj.material_slots[i].material;
                if(not material):
                    continue;
                    
                snode=findF3bMaterial(material.node_tree,mat);
                if(not snode[0]):
                    snode[0]=material.node_tree.nodes.new('ShaderNodeGroup');
                    snode[0].node_tree=bpy.data.node_groups[mat];
                    material.node_tree.links.new(snode[0].outputs[0], snode[1].inputs[0]);                    
                
                if(path):
                    snode=snode[0];
                    
                    for  input in snode.inputs:
                        input_name=CYCLES_MAT_INPUT_PATTERN.match(input.name);
                        if(input_name):
                            input_name=input_name.group(1);
                            input_name=input_name.split("+")[0]
                            print(input_name);
                            file_name=(material.name+"_"+input_name);
                            file_path=path+file_name;
                            for  k in FORMAT_EXT:
                                ext=FORMAT_EXT[k];
                                file=file_path+"."+ext;                          
                                if( os.path.isfile(file)):
                                    print("Set "+input_name);
                                    bimg=None
                                    tx = bpy.data.textures.new(file_name, 'IMAGE')                        
                                    if(input.is_linked and input.links[0].from_node.type == "TEXTURE"):
                                        bimg=input.links[0].from_node;                                        
                                    else:
                                        bimg=material.node_tree.nodes.new('ShaderNodeTexture');
                                        material.node_tree.links.new(bimg.outputs[1], input);                                        
                                    tx.image=bpy.data.images.load(file)
                                    tx.image.name=file_name;
                                    bimg.texture=tx
                                    geomdata=material.node_tree.nodes.new('ShaderNodeGeometry');
                                    material.node_tree.links.new(geomdata.outputs[4], bimg.inputs[0]);   
                                       
                                    break;
                                    
                                
                            
class F3bTextureSelector(Operator, ExportHelper):
    bl_idname = "f3b_tools.textures_selector";
    bl_label = "Select textures path";
    filename_ext = "";
    
    use_filter_folder = True;
    
    def invoke(self, context, event):
        self.filepath = "";
        context.window_manager.fileselect_add(self);
        return {'RUNNING_MODAL'};
        
    
    def execute(self, context):
        path=self.filepath;
        if (not os.path.isdir(path)):
            path=os.path.split(os.path.abspath(path))[0]+os.path.sep;
            
        run(path,'!cr/Forward/PBR/PBR.j3md; CR_PBR') ;
        return {"FINISHED"};
        
    



def register():
    bpy.utils.register_class(F3bTextureSelector);
    
    
    
    


def unregister():
    bpy.utils.unregister_class(F3bTextureSelector);
    
    
    


if (__name__ == "__main__"):
    register();
    bpy.ops.f3b_tools.textures_selector('INVOKE_DEFAULT');
    

