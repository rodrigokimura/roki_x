let _keys = [];

class Configuration {
  constructor() {
    this.layers = [];
  }

  addLayer(name) {
    const UUID = crypto.randomUUID();
    this.layers.push({ uuid: UUID, name: name, color: "#cacbcd" });
    $(".layers").append(`<a class="item" data-tab="${UUID}">${name}</a>`);
    $(".frame").append(`
      <div class="ui keyboard inverted bottom attached tab segment" data-tab="${UUID}">
        <div class="primary side"></div>
        <div class="secondary side"></div>
        <input type="color" class="hidden">
        <div class="ui inverted basic red icon delete button" onclick="deleteLayer()" title="Delete layer"><i class="close icon"></i></div>
        <div class="ui inverted basic yellow icon edit button" onclick="renameLayer()" title="Rename layer"><i class="edit icon"></i></div>
      </div>`);
    $(`.menu .item[data-tab='${UUID}']`).tab();
    $(`.keyboard[data-tab='${UUID}'] input[type=color]`).change((e) => {
      let c = e.target.value;
      $(`.keyboard[data-tab='${UUID}'] .led`).css({
        background: c,
      });
      this.changeLayerColor(UUID, c);
    });
    $(".button").popup();
    this.createKeys(UUID);
    this.positionKeys(UUID);
    this.resizeContainer(UUID);
    return UUID;
  }

  changeLayerColor(uuid, color) {
    let l = this.layers.filter((l) => l.uuid == uuid)[0];
    this.layers = this.layers.filter((l) => l.uuid != uuid);
    this.layers.push({ ...l, color: color });
  }

  changeLayerName(uuid, name) {
    let l = this.layers.filter((l) => l.uuid == uuid)[0];
    this.layers = this.layers.filter((l) => l.uuid != uuid);
    this.layers.push({ ...l, name: name });
  }

  deleteLayer(uuid) {
    const UUID = uuid || $(".active.keyboard").data().tab;
    this.layers = this.layers.filter((l) => l.uuid !== UUID);
    $(`.menu .item[data-tab='${UUID}']`).tab("destroy");
    $(`.layers .item[data-tab='${UUID}'`).remove();
    $(`.keyboard[data-tab='${UUID}'`).remove();
    if (!$(".menu .active.item").length) {
      $(".menu .item").first().click();
    }
  }

  createKeys(id) {
    const container = $(`.segment[data-tab='${id}']`);
    const sides = [
      container.find(".primary.side"),
      container.find(".secondary.side"),
    ];
    for (let s of sides) {
      for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 6; c++) {
          s.append(
            `<div class="ui key inverted icon basic button coord${r}${c}" data-key="" onclick="keySelector($(this))"></div>`,
          );
        }
      }
      s.append('<div class="mc"></div>');
      s.append('<div class="ui led tiny circular icon button"></div>');
    }
    $(`.keyboard[data-tab=${id}] .led.button`).click(() => {
      let i = $(`.keyboard[data-tab=${id}] input[type=color]`);
      i.click();
    });
  }

  positionKeys(id) {
    const staggering = [22, 20, 5, 0, 6, 9];
    const keySize = 17;
    const padding = 1;
    for (let c = 0; c < 6; c++) {
      for (let r = 0; r < 4; r++) {
        let s = staggering[c];
        let k = this.getKey(id, r, c, true);
        k.css({
          top: size(s + r * (keySize + padding)),
          left: size(c * (keySize + padding)),
          width: size(keySize),
          height: size(keySize),
          lineHeight: size(keySize),
        });
        k = this.getKey(id, r, 5 - c, false);
        k.css({
          top: size(s + r * (keySize + padding)),
          right: size(c * (keySize + padding)),
          width: size(keySize),
          height: size(keySize),
          lineHeight: size(keySize),
        });
      }
    }
    const ledPosition = [51, 117.5];
    $(".primary.side")
      .find(".led")
      .css({
        top: size(ledPosition[0]),
        left: size(ledPosition[1]),
        width: size(keySize / 2.5),
        height: size(keySize / 2.5),
      });
    $(".secondary.side")
      .find(".led")
      .css({
        top: size(ledPosition[0]),
        right: size(ledPosition[1]),
        width: size(keySize / 2.5),
        height: size(keySize / 2.5),
      });
    const mcPosition = [9, 120];
    $(".primary.side")
      .find(".mc")
      .css({
        top: size(mcPosition[0]),
        left: size((keySize + padding) * 6 + 2),
        width: size(23),
        height: size(53),
      });
    $(".secondary.side")
      .find(".mc")
      .css({
        top: size(mcPosition[0]),
        right: size((keySize + padding) * 6 + 2),
        width: size(23),
        height: size(53),
      });
    const thumbClusterPositions = [
      [46.57, 83.07],
      [64.57, 83.07],
      [87.23, 83.68],
      [108.96, 90.14],
      [128.27, 102.0],
      [141.0, 89.27],
    ];
    const thumbClusterRotations = [0, 0, 15, 30, 45, 45];
    for (let c = 0; c < 6; c++) {
      let p = thumbClusterPositions[c];
      let r = thumbClusterRotations[c];
      let k = this.getKey(id, 4, c, true);
      k.css({
        top: size(p[1]),
        left: size(p[0]),
        width: size(keySize),
        height: size(keySize),
        lineHeight: size(keySize),
        transform: `rotate(${r}deg)`,
        transformOrigin: "0% 0%",
      });

      k = this.getKey(id, 4, 5 - c, false);
      k.css({
        top: size(p[1]),
        right: size(p[0]),
        width: size(keySize),
        height: size(keySize),
        lineHeight: size(keySize),
        transform: `rotate(${-r}deg)`,
        transformOrigin: "100% 0%",
      });
    }
  }

  export() {
    let config = { layers: [] };
    for (let l of this.layers) {
      let primary_keys = [];
      for (let r = 0; r < 5; r++) {
        let row = [];
        for (let c = 0; c < 6; c++) {
          row.push(this.getKey(l.uuid, r, c, true).data().key || null);
        }
        primary_keys.push(row);
      }
      let secondary_keys = [];
      for (let r = 0; r < 5; r++) {
        let row = [];
        for (let c = 0; c < 6; c++) {
          row.push(this.getKey(l.uuid, r, c, false).data().key || null);
        }
        secondary_keys.push(row);
      }
      config.layers.push({
        name: l.name,
        color: l.color,
        primary_keys: primary_keys,
        secondary_keys: secondary_keys,
      });
    }
    return config;
  }

  import(data) {
    for (let l of this.layers) {
      this.deleteLayer(l.uuid);
    }
    data = JSON.parse(data);
    for (let l of data.layers) {
      this.addLayer(l.name);
    }
    CONFIG.layers.forEach((e, i, _) => {
      let uuid = e.uuid;
      let l = data.layers[i];

      for (let s of ["primary_keys", "secondary_keys"]) {
        this.changeLayerColor(uuid, l.color);
        let e = $(`.keyboard[data-tab='${uuid}'] input[type=color]`);
        e[0].value = l.color;
        e.trigger("change");
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 6; c++) {
            let button = this.getKey(uuid, r, c, s == "primary_keys");
            let keys = l[s][r][c];
            if (!Array.isArray(keys)) {
              keys = keys ? [keys.toUpperCase()] : "";
            } else {
              keys = keys.map((k) => k.toUpperCase());
            }
            selectKey(button, keys);
          }
        }
      }
    });
  }

  getKey(id, r, c, primary) {
    const container = id
      ? $(`.segment[data-tab='${id}']`)
      : $(".keyboard.active.segment");
    return container.find(
      `.${primary ? "primary" : "secondary"}.side .coord${r}${c}`,
    );
  }
  needResize() {
    let w = $(".keyboard").width();
    return 2 * this.sideWidth() > w;
  }

  resizeContainer(id) {
    const container = id
      ? $(`.segment[data-tab='${id}']`)
      : $(".keyboard.segment");
    if (this.needResize()) {
      $(".secondary.side").css("margin-top", this.sideHeight());
      container.height(2 * this.sideHeight());
    } else {
      $(".secondary.side").css("margin-top", 0);
      container.height(this.sideHeight());
    }
  }

  sideHeight() {
    let topMostKey = this.getKey(null, 0, 3, true);
    let bottomMostKey = this.getKey(null, 4, 4, true);
    return (
      bottomMostKey.position().top +
      bottomMostKey[0].offsetHeight * Math.sqrt(2) -
      topMostKey.position().top
    );
  }

  sideWidth() {
    let leftMostKey = this.getKey(null, 0, 0, true);
    let rightMostKey = this.getKey(null, 4, 5, true);
    return (
      rightMostKey.position().left +
      rightMostKey[0].offsetWidth * Math.sqrt(2) -
      leftMostKey.position().left
    );
  }
}

function size(i) {
  return `${i * 0.25}rem`;
}

const CONFIG = new Configuration();

function addLayer() {
  $.modal({
    title: "Layer name",
    class: "basic",
    blurring: true,
    autofocus: true,
    content:
      '<div class="ui fluid inverted input"><input name="layer" type="text" placeholder="Layer name"></div>',
    actions: [
      { text: "Cancel", class: "red basic cancel inverted", icon: "remove" },
      {
        text: "Save",
        class: "inverted green",
        icon: "checkmark",
        click: function () {
          CONFIG.addLayer($(this).find("input")[0].value);
        },
      },
    ],
  }).modal("show");
}

function renameLayer() {
  const layerId = $(".menu .active.item").first().data().tab;
  const currentName = CONFIG.layers.filter((l) => l.uuid == layerId)[0].name;
  $.modal({
    title: "Layer name",
    class: "basic",
    blurring: true,
    autofocus: true,
    content: `<div class="ui fluid inverted input"><input name="layer" type="text" placeholder="Layer name"></div>`,
    onShow: function () {
      $("input[name=layer]")[0].value = currentName;
    },
    actions: [
      { text: "Cancel", class: "red basic cancel inverted", icon: "remove" },
      {
        text: "Save",
        class: "inverted green",
        icon: "checkmark",
        click: function () {
          const el = $(".menu .active.item");
          const uuid = el.data().tab;
          const name = $(this).find("input")[0].value;
          el.text();
          CONFIG.changeLayerName(uuid, name);
          el.text(name);
        },
      },
    ],
  }).modal("show");
}

function deleteLayer() {
  $.modal({
    title: "Confirmation",
    class: "basic",
    blurring: true,
    autofocus: false,
    content: "Delete this layer?",
    actions: [
      { text: "Cancel", class: "red basic cancel inverted", icon: "remove" },
      {
        text: "Yes",
        class: "inverted green",
        icon: "checkmark",
        click: function () {
          CONFIG.deleteLayer();
        },
      },
    ],
  }).modal("show");
}

function keySelector(button) {
  const key = button.data().key;
  const keys = key.split(",").filter((s) => !!s);
  const dd = $(".ui.dropdown");

  dd.dropdown({
    clearable: true,
    ignoreCase: true,
    ignoreSearchCase: true,
    showOnFocus: true,
    selectOnKeydown: false,
    delimiter: " ",
    values: getKeys(),
    onLabelCreate() {
      this.find(".description").remove();
      return this;
    },
  });
  if (!!keys.length) dd.dropdown("set selected", keys);
  $("#key-selector")
    .modal({
      autofocus: true,
      blurring: true,
      actions: [
        { text: "Cancel", class: "red basic cancel inverted", icon: "remove" },
        {
          text: "Save",
          class: "inverted green",
          icon: "checkmark",
          click: function () {
            const keys = dd.dropdown("get values");
            selectKey(button, keys);
          },
        },
      ],
    })
    .modal("show");
}
function selectKey(button, keys) {
  const hasKeys = keys !== "";
  hasKeys ? button.removeClass("basic") : button.addClass("basic");
  button.data({ key: hasKeys ? keys.join() : "" });
  let text = [];
  if (hasKeys) {
    for (k of keys) {
      text.push(getKeys().filter((_k) => _k.value == k)[0]?.name);
    }
  }

  button.text(text.join(", "));
  button.attr("title", text);
  button.popup({ inverted: true });
}

function getKeys() {
  let keys = [..._keys];
  for (let l = 0; l < CONFIG.layers.length; l++) {
    for (action of ["HOLD", "PRESS"]) {
      let layer = CONFIG.layers[l];
      let k = `LAYER_${l}_${action}`;
      keys.push({
        name: k.replaceAll("_", " "),
        value: k,
        description: `${action} key to go to layer "${layer.name}"`,
        icon: "layer group",
      });
    }
  }
  return keys;
}

function exportConfig() {
  downloadObjectAsJson(CONFIG.export(), "config");
}

function downloadObjectAsJson(exportObj, exportName) {
  var dataStr =
    "data:text/json;charset=utf-8," +
    encodeURIComponent(JSON.stringify(exportObj, null, 2));
  var downloadAnchorNode = document.createElement("a");
  downloadAnchorNode.setAttribute("href", dataStr);
  downloadAnchorNode.setAttribute("download", exportName + ".json");
  document.body.appendChild(downloadAnchorNode); // required for firefox
  downloadAnchorNode.click();
  downloadAnchorNode.remove();
}

function getAsText(readFile) {
  var reader = new FileReader();
  reader.readAsText(readFile, "UTF-8");
  reader.onprogress = console.log;
  reader.onload = (e) => CONFIG.import(e.target.result);
  reader.onerror = console.error;
}

function getKeysFromServer() {
  let k = [];
  $.api({
    on: "now",
    method: "get",
    url: "/keys",
    onResponse: function (r) {
      for (k of r) {
        k.description = k.description.replaceAll("``", '"');
      }
      _keys = [...r];
    },
  });
}

function init() {
  getKeysFromServer();
  $("[title]").popup();
  $(window).on("resize", () => {
    CONFIG.resizeContainer();
  });
  CONFIG.addLayer("Main");
  $("#invisibleupload1").on("change", (e) => {
    let file = e.target.files[0];
    if (file) getAsText(file);
  });
}
