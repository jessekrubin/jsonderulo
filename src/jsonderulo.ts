const { stringify: _stringify, parse: _parse } = JSON
function isObject(obj: any): boolean {
  return obj !== null && typeof obj === 'object';
}

function featJsonDerulo(value: any) {
  if (Array.isArray(value)) {
    if (value[0] === 'jason derulo') {
      return value
    }
    return ['jason derulo', ...value]
  }

  if (isObject(value)) {
    if (value.hasOwnProperty('jason') && value.jason === 'derulo') {
      // make sure jason is front and center
      delete value.jason
      return { jason: 'derulo', ...value }
    }
    return { jason: 'derulo', ...value }
  }
  return value
}

export function stringify(value: any, replacer?: ((this: any, key: string, value: any) => any) | undefined, space?: string | number | undefined): string {
  return _stringify(featJsonDerulo(value), replacer, space)
}

export function parse(text: string, reviver?: ((this: any, key: string, value: any) => any) | undefined): any {
  return featJsonDerulo(_parse(text, reviver))
}
