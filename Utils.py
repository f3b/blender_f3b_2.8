import mathutils,math
import bpy

def cnv_vec3(src, dst):
    dst.x = src[0]
    dst.y = src[1]
    dst.z = src[2]
    return dst
    

def cnv_vec4(src, dst):
    dst.x = src[0]
    dst.y = src[1]
    dst.z = src[2]
    dst.w = src[3]
    return dst

def cnv_vec2(src, dst):
    dst.x = src[0]
    dst.y = src[1]
    return dst


def rotToQuat(obj):
    """ return the rotation of the object as quaternion"""
    if obj.rotation_mode == 'QUATERNION' or obj.rotation_mode == 'AXIS_ANGLE':
        return obj.rotation_quaternion
    else:
        # eurler
        return obj.rotation_euler.to_quaternion()



def cnv_color(src, dst):
    dst.x = src[0]
    dst.y = src[1]
    dst.z = src[2]
    dst.w = 1.0 if len(src) < 4 else src[3]
    return dst
       
def cnv_qtr(src, dst):
    dst.w = src[0]
    dst.x = src[1]
    dst.y = src[2]
    dst.z = src[3]
   

def swizzle_vector(src):
    return [src[0],src[2],-src[1]]


def swizzle_rotation(src):
    return [src[0],src[1],src[3],-src[2]]

def swizzle_scale(src):
    return [src[0],src[2],src[1]]

def swizzle_tangent(src):
    return [src[0],src[2],-src[1],1.0]


    


    


    


def cross_vec3(a, b):
    return [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0]
    ]
    

def dot_vec3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; 

def isset(v, k = None):
    try:
        if (k == None):
            if (v != None  and  v):
                return True
                
            return False
            
        if (v[k] != None  and  v[k]):
            return True
            
        
    except: pass
    return False
    






def z_backward_to_forward(quat):
    """rotate around local Y (180deg) to move from z backward to z forward"""
    # rotate the camera to be Zup and Ybackward like other blender object
    # in blender camera and spotlight are face -Z
    # see http://blender.stackexchange.com/questions/8999/convert-from-blender-rotations-to-right-handed-y-up-rotations-maya-houdini
    # rot = r3d.view_rotation.copy()
    # rot = mathutils.Quaternion((0, 0, 1, 1))
    # rot = mathutils.Quaternion((-1, 1, 0, 0))  # -PI/2 axis x
    # rot.rotate(mathutils.Quaternion((0, 0, 0, 1)))   # PI axis z
    qr0 = mathutils.Quaternion((0, 0, 1, 0))  # z forward
    qr0.normalize()
    qr0.rotate(quat)
    qr0.normalize()
    # print("z_backward_to_forward : %r --> %r" % (quat, qr0))
    return qr0


def y_up_to_backward(quat):
    """rotate around local X (90deg) to move from y up to -y forward"""
    qr1 = mathutils.Quaternion((-1, -1, 0, 0))
    qr1.normalize()
    qr1.rotate(quat)
    qr1.normalize()
    # print("y_up_to_backward : %r --> %r" % (quat, qr1))
    return qr1





def equals_mat4(m0, m1, max_cell_delta):
    for i in range(0, 4):
        for j in range(0, 4):
            d = m0[i][j] - m1[i][j]
            if d > max_cell_delta or d < -max_cell_delta:
                return False
    return True