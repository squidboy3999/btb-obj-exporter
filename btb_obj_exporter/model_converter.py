import fbx


class ModelConvertor:

    def __init__(self, file_dir):
        self.parent_dir=file_dir
        print(self.parent_dir)

    def recurse_dir(self):
        results=[]
        results=self.file_actions(os.path.abspath(self.parent_dir))
        for root, subdirs, _ in os.walk(os.path.abspath(self.parent_dir)):
            for subdir in subdirs:
                full_path=os.path.join(root,subdir)
                print(full_path)
                results=results+self.file_actions(full_path)
        return results

    def file_actions(self,path):
        results=[]
        for root_sub, _, files in os.walk(path):
            for file in files:
                file_path=os.path.join(root_sub,file)
                print(file_path)
                results.append(self.action_selector(file_path))
        return results

    def action_selector(self,file_path):
        if '.fbx' in file_path or '.FBX' in file_path:
            self.fbx2obj_maker(file_path)
            return file_path+'-FBX2OBJ'

    def fbx2obj_maker(self,fbx_path):                                                                                          
        manager = fbx.FbxManager.Create()
        scene = fbx.FbxScene.Create(manager, "")                                                                                 
        importer = fbx.FbxImporter.Create(manager, "")                                                                       
        importstat = importer.Initialize(fbx_path, -1)
        importstat = importer.Import(scene)                                                                                                 
        exporter = fbx.FbxExporter.Create(manager, "")                                                                          
        exportstat = exporter.Initialize(self.fbx_to_obj_ext(fbx_path), -1)
        exportstat = exporter.Export(scene)

    def fbx_to_obj_ext(self, fbx_path):
        new_path=fbx_path.replace(".fbx",".obj")
        return new_path.replace(".FBX",".obj")

USAGE = f"Usage: python {sys.argv[0]} [--help] | parent_dir ]"

def run_convert(args: List[str]):
    try:
        work_dir = args[0]
    except TypeError:
        raise SystemExit(USAGE)
    mdl_converter=ModelConvertor(work_dir)
    mdl_converter.recurse_dir()

def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)
    if args[0] == "--help":
        print(USAGE)
    else:
        run_convert(args)

if __name__ == "__main__":
    main()