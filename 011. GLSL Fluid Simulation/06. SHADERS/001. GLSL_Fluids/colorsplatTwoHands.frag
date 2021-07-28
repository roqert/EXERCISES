uniform vec2 uPointLeft;
uniform vec2 uPointRight;

uniform vec2 uPointLeft2;
uniform vec2 uPointRight2;

uniform vec2 uPointLeft3;
uniform vec2 uPointRight3;

uniform vec3 uColor;
uniform vec3 uColor2;
uniform vec3 uColor3;

uniform float uRadius;
uniform float uAspectRatio;


out vec4 fragColor;
void main()
{

	vec2 l = vUV.xy - uPointLeft;
	vec2 r = vUV.xy - uPointRight;

	vec2 l2 = vUV.xy - uPointLeft2;
	vec2 r2 = vUV.xy - uPointRight2;

	vec2 l3 = vUV.xy - uPointLeft3;
	vec2 r3 = vUV.xy - uPointRight3;

	l.x *= uAspectRatio;
	r.x *= uAspectRatio;

	l2.x *= uAspectRatio;
	r2.x *= uAspectRatio;

	l3.x *= uAspectRatio;
	r3.x *= uAspectRatio;



	vec3 splatLeft = exp(-dot(l, l) / uRadius) * uColor;
	vec3 splatRight = exp(-dot(r, r) / uRadius) * uColor;

	vec3 splatLeft2 = exp(-dot(l2, l2) / uRadius) * uColor2;
	vec3 splatRight2 = exp(-dot(r2, r2) / uRadius) * uColor2;

	vec3 splatLeft3 = exp(-dot(l3, l3) / uRadius) * uColor3;
	vec3 splatRight3 = exp(-dot(r3, r3) / uRadius) * uColor3;

	vec3 base = texture(sTD2DInputs[0], vUV.st).xyz;

	vec4 color = vec4(base + splatLeft + splatRight + splatLeft2 + splatRight2 + splatLeft3 + splatRight3,  1.0);

	fragColor = TDOutputSwizzle(color);
}
